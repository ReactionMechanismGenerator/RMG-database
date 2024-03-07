#!/usr/bin/env python
# encoding: utf-8


name = "SurfaceThermoPt111"
shortDesc = u"Surface adsorbates on Pt(111)"
longDesc = u"""
Surface species adsorbed on Pt(111). The thermochemistry of all adsorbates with up to 2 heavy atoms was calculated by Katrin Blondal at Brown University around 2018,
based on DFT calculations by Jelena Jelic at KIT. See https://doi.org/10.1021/acs.iecr.9b01464 for the details on the computational methods as well as the results.
This database was extended with DFT calculations for larger adsorbates by Bjarne Kreitz (Brown University).  
The computational methods for the extension are explained in detail in https://doi.org/10.1021/acscatal.2c03378. If you use this database in your work, please cite the publications mentioned above. 
Note: X indicates a bond to the surface. It is always on the left hand site of an atom that is bonded to the surface e.g. XCCH2 it means that C is bonded to the surface.
If the X is on the right hand side and at the end of a label, it means that this species is physisorbed. 
"""

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
    label = "XH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
       polynomials = [
        NASAPolynomial(coeffs=[-2.07570125E+00, 1.73580835E-02, -2.60920784E-05, 1.89282268E-08, -5.38835643E-12, -3.16618959E+03, 8.15361518E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[2.72248139E+00, -1.06817206E-03, 1.98653790E-06, -1.12048461E-09, 2.09811636E-13, -4.21823896E+03, -1.53207470E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.481 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "H2X",
    molecule =
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
    	polynomials = [
        NASAPolynomial(coeffs=[3.86406413E+00, 7.53456449E-04, -1.65571442E-06, 1.55223217E-09, -4.46782260E-13, -1.68927505E+03, -8.85806531E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[4.06879652E+00, -4.95806734E-04, 6.59234335E-07, -1.72597715E-10, 7.62965383E-15, -1.70070035E+03, -9.71917749E+00], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.051 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "H2OX",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.72971388E+00, 8.71051652E-03, -1.29131826E-05, 1.07295000E-08, -3.39433689E-12,
                                   -3.26126997E+04, -6.04479516E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.85496280E+00, -3.28847412E-03, 5.56990501E-06, -2.73008086E-09, 4.55898028E-13,
                                   -3.33046343E+04, -2.13518349E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.189 eV.

                The two lowest frequencies, 12.0 and 62.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 5,
    label = "XOH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.42359828E+00, 1.57830409E-02, -2.91659307E-05, 2.50432531E-08, -8.04088046E-12,
                                   -1.89993029E+04, -3.15230478E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.03574444E+00, -1.34422013E-03, 2.25915779E-06, -1.08547653E-09, 1.77875516E-13,
                                   -1.96344169E+04, -2.00345222E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.628 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 6,
    label = "HOOHX",
    molecule =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.96560716E+00, 1.33978369E-02, -1.34293557E-05, 7.12175948E-09, -1.41063029E-12,
                                   -2.52496080E+04, -6.15466087E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.63537655E+00, -4.64148419E-03, 8.09255957E-06, -4.16762137E-09, 7.26386983E-13,
                                   -2.66787468E+04, -3.48128042E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.285 eV.

                The two lowest frequencies, 12.0 and 47.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 7,
    label = "XOXO",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[9.67032554E-01, 2.01073426E-02, -3.43087565E-05, 2.75767553E-08, -8.53056861E-12,
                                   -1.38224268E+04, -5.63546035E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.80193269E+00, -7.29910156E-04, 1.37020436E-06, -7.76162799E-10, 1.45741297E-13,
                                   -1.47787200E+04, -2.87540997E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.232 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 8,
    label = "XOOH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.72534279E+00, 1.42651752E-02, -2.21410322E-05, 1.71597713E-08, -5.14814406E-12,
                                   -1.59330066E+04, -5.88006622E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.85340011E+00, -2.06281219E-03, 3.57770248E-06, -1.82187965E-09, 3.14702407E-13,
                                   -1.68171383E+04, -2.59655505E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.205 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 9,
    label = "XO",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.94475701E-01, 1.44162624E-02, -2.61322704E-05, 2.19005957E-08, -6.98019420E-12,
                                   -1.64619234E+04, -1.99445623E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.90244691E+00, -3.38584457E-04, 6.43372619E-07, -3.66326660E-10, 6.90093884E-14,
                                   -1.70497471E+04, -1.52559728E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.101 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 10,
    label = "XONH2",
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
            NASAPolynomial(coeffs=[2.40658689E+00, 1.61838708E-02, -1.58074626E-05, 8.48925729E-09, -1.83038307E-12, -8.83680682E+03, -7.56970401E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.42636683E+00, -5.74378741E-03, 1.01435819E-05, -5.32742710E-09, 9.43135142E-13, -1.06436383E+04, -4.31963080E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
    label = "XOCH3",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.63812716E+00, 1.12365450E-02, 3.66483568E-06, -1.11206508E-08, 4.85717369E-12,
                                   -2.00034033E+04, -2.01845704E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.02529575E+01, -9.48030603E-03, 1.69012340E-05, -9.01198807E-09, 1.61413339E-12,
                                   -2.25504985E+04, -4.73210723E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.800 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 12,
    label = "NH3X",
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
    label = "XNH2",
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
    label = "XNH",
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
    label = "XN",
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
    label = "H2NOHX",
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
    label = "HNOX",
    molecule =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.01921333E+00, 1.32114264E-02, -1.38865889E-05, 8.22652454E-09, -2.08098816E-12, -8.20311734E+03, -7.36585771E+00], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.47524494E+00, -3.96252296E-03, 7.10187157E-06, -3.81135483E-09, 6.86348467E-13, -9.61232525E+03, -3.50542775E+01], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (2000.0, 'K'),
    ),
    longDesc = u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (file: compute_NASA_for_Pt-adsorbates.ipynb). 
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "HXNOH",
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
    label = "XNO",
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
    label = "XNXO",
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
    label = "XNOH",
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
    label = "NH2NH2X",
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
    label = "NHNHX",
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
    label = "NNX",
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
    label = "XNHNH2",
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
    label = "XNNH_ads",
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
    label = "XNNH2",
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
    label = "XNHXNH",
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
    label = "XNHXN",
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
    label = "XNHCH3",
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
    label = "XNCH2",
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
    label = "XNCH3",
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
    label = "XC",
    molecule =
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.94350915E+00, 1.97767398E-02, -3.36336641E-05, 2.69027201E-08, -8.27959229E-12,
                                   7.00056568E+03, 7.17469909E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.81347137E+00, -6.93951702E-04, 1.30307929E-06, -7.38700347E-10, 1.38795827E-13,
                                   6.06002730E+03, -1.55738286E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -7.665 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 35,
    label = "XCXC",
    molecule =
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.57614736E-01, 1.93811681E-02, -2.99692178E-05, 2.27772298E-08, -6.82679954E-12,
                                   2.49318311E+04, -2.70419665E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.60814537E+00, -1.42377339E-03, 2.64198198E-06, -1.48289867E-09, 2.76540004E-13,
                                   2.37577354E+04, -2.88541367E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.388 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 36,
    label = "XCCH2",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D} {4,S} {5,S}
4 H  u0  p0 c0 {3,S}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.53720415E-01, 2.73804858E-02, -3.86126272E-05, 2.92701452E-08, -8.86074894E-12,
                                   1.25631140E+04, -2.85681996E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50738185E+00, -5.96520880E-03, 1.06150068E-05, -5.63034056E-09, 1.00413592E-12,
                                   1.04252330E+04, -4.81889215E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.610 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 37,
    label = "XCCH3",
    molecule =
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.98832282E-01, 2.20312098E-02, -1.63022134E-05, 5.40142239E-09, -2.95003605E-13,
                                   -1.13206275E+04, -3.41231804E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.13080922E+01, -9.36315902E-03, 1.67090264E-05, -8.91840540E-09, 1.59869331E-12,
                                   -1.42352321E+04, -5.58203537E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.087 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 38,
    label = "XCH",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.66805027E+00, 2.90693485E-02, -4.82653552E-05, 3.87589256E-08, -1.19749384E-11,
                                   -2.91815541E+03, 9.72941427E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.90429859E+00, -2.63865042E-03, 4.71729273E-06, -2.51267002E-09, 4.49659283E-13,
                                   -4.46440812E+03, -2.67107945E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.820 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 39,
    label = "XCHXCH",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-3.12098801E+00, 3.94849074E-02, -5.46713780E-05, 3.87299954E-08, -1.08911005E-11,
                                   4.51944481E+02, 1.11984198E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50734934E+00, -6.29448074E-03, 1.12600196E-05, -6.02346339E-09, 1.08201133E-12,
                                   -2.47008905E+03, -5.12968133E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.907 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 40,
    label = "CHCHX",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.72394638E-01, 2.77615066E-02, -4.48825330E-05, 3.68137777E-08, -1.16132416E-11,
                                   2.05362649E+04, 2.41179267E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.53228490E+00, -4.93781260E-03, 8.64081750E-06, -4.46203746E-09, 7.78651886E-13,
                                   1.88254924E+04, -3.66656813E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.160 eV.

                The two lowest frequencies, 12.0 and 90.3 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 41,
    label = "XCH2",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.23006757E+00, 2.92222928E-02, -4.33154923E-05, 3.31428193E-08, -9.96471308E-12,
                                   -2.22255986E+02, 8.30173205E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.83459954E+00, -5.14926339E-03, 9.15491022E-06, -4.84917377E-09, 8.63766547E-13,
                                   -2.25897684E+03, -3.62215373E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.305 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 42,
    label = "XCH2XCH2",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.67192340E+00, 3.80645196E-02, -3.82436290E-05, 2.04023322E-08, -4.28929114E-12,
                                   -8.53533882E+03, 1.05040932E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.32289950E+01, -1.18706595E-02, 2.11521655E-05, -1.12641620E-08, 2.01566940E-12,
                                   -1.26116343E+04, -7.01190196E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.927 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 43,
    label = "XCH3",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-4.44549060E-02, 1.94367665E-02, -1.91028733E-05, 1.11269371E-08, -2.73735895E-12,
                                   -6.38803762E+03, -1.73375969E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.65704524E+00, -7.90307778E-03, 1.40100438E-05, -7.40016074E-09, 1.31516592E-12,
                                   -8.63598517E+03, -4.43352558E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.721 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 44,
    label = "CH3CH3X",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.21371476E+00, 1.22146805E-02, 1.90686655E-05, -2.86454335E-08, 1.10578994E-11,
                                   -1.47557767E+04, -3.32732546E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.58691357E+01, -1.76783249E-02, 3.14415254E-05, -1.67061667E-08, 2.98335715E-12,
                                   -1.89588898E+04, -7.59101763E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.192 eV.

                The two lowest frequencies, 12.0 and 77.2 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 45,
    label = "CH4X",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.85496247E+00, -5.54134984E-03, 3.01198105E-05, -2.99225917E-08, 1.00502514E-11,
                                   -1.17096278E+04, -9.25620913E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.54139378E+00, -1.04025134E-02, 1.83777400E-05, -9.66765130E-09, 1.71211379E-12,
                                   -1.34475614E+04, -3.55638434E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.125 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 46,
    label = "XCN",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,T}
3 N  u0  p1 c0 {2,T}
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
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.64671 eV, gamma_C(X) = 0.250.""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
    label = "XCNH",
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
    label = "XCNH2",
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
    label = "XCO",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.42895000E+00, 1.40374509E-02, -2.21178920E-05, 1.78659581E-08, -5.71478802E-12,
                                   -3.45688484E+04, -7.78265517E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.48656312E+00, -1.68118543E-03, 3.09030310E-06, -1.71186643E-09, 3.15864598E-13,
                                   -3.54815495E+04, -2.76788365E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.415 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 50,
    label = "XCOH",
    molecule =
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.81392618E-01, 2.36060988E-02, -3.32958929E-05, 2.35937581E-08, -6.59988036E-12,
                                   -3.04499080E+04, -2.84937962E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.57277703E+00, -3.16578469E-03, 5.61811938E-06, -2.96831946E-09, 5.28683990E-13,
                                   -3.21118815E+04, -3.88297167E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.708 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 51,
    label = "XCH2XCH",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-4.49841757E+00, 4.74505397E-02, -6.33178372E-05, 4.41445511E-08, -1.23100766E-11,
                                   -2.72259790E+03, 1.69502146E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.14364336E+01, -9.00409564E-03, 1.60927814E-05, -8.59946878E-09, 1.54310894E-12,
                                   -6.48496972E+03, -6.22564682E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.339 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 52,
    label = "XCH2CH3",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.18934574E-01, 2.54180961E-02, -9.60812964E-06, -4.29518553E-09, 3.46436421E-12,
                                   -1.06881806E+04, -7.38059313E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.50607717E+01, -1.48576350E-02, 2.64630769E-05, -1.40881129E-08, 2.51997894E-12,
                                   -1.48787788E+04, -7.82120803E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.301 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 53,
    label = "CH2NHX",
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
    label = "XCH2NH2",
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
    label = "CH2OX",
    molecule =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.15211100E+00, -5.48713399E-04, 1.68589310E-05, -1.83357871E-08, 6.29630397E-12,
                                   -2.10010697E+04, -1.14420380E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.40512532E+00, -6.90216938E-03, 1.23521550E-05, -6.62362990E-09, 1.19136449E-12,
                                   -2.24821487E+04, -3.48417937E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.161 eV.

                The two lowest frequencies, 12.0 and 51.8 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 56,
    label = "XCH2OH",
    molecule =
"""
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-3.73829188E-01, 2.33977003E-02, -1.95735792E-05, 7.62721113E-09, -7.42114703E-13,
                                   -2.93842663E+04, 6.57911397E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.03141499E+01, -8.56871933E-03, 1.51855306E-05, -8.02279311E-09, 1.42722033E-12,
                                   -3.21967714E+04, -4.79896307E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.347 eV.

                The two lowest frequencies, 25.3 and 72.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 57,
    label = "XCH2XN",
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
    label = "XCH2XNH",
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
    label = "CH3NH2X",
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
    label = "CH3OHX",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.05737703E+00, 1.28624334E-02, 4.84927639E-06, -1.35997111E-08, 5.96900307E-12,
                                   -3.10621321E+04, -1.24359019E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.31134924E+01, -1.14087964E-02, 2.02030110E-05, -1.06647877E-08, 1.89545946E-12,
                                   -3.40195663E+04, -6.52666455E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.304 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 61,
    label = "XCHXC",
    molecule =
"""
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-5.90352229E-01, 2.82029410E-02, -4.31920779E-05, 3.32067162E-08, -1.00161719E-11,
                                   1.45622398E+04, 2.24767212E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.59299131E+00, -3.51002045E-03, 6.29100233E-06, -3.36852902E-09, 6.05610928E-13,
                                   1.27604716E+04, -3.97960433E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -4.559 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 62,
    label = "XCHCH2",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 H  u0  p0 c0 {2,S}
5 H  u0  p0 c0 {3,S}
6 H  u0  p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-3.08859296E-01, 2.83916975E-02, -3.01517554E-05, 1.77197656E-08, -4.27593030E-12,
                                   2.57912056E+03, 1.02855689E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.13486298E+01, -8.90556058E-03, 1.58461696E-05, -8.41756550E-09, 1.50324475E-12,
                                   -3.83883430E+02, -5.79325796E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.860 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 63,
    label = "XCHCH3",
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
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.02964656E+00, 3.05643757E-02, -2.57333903E-05, 1.12938139E-08, -1.82181353E-12,
                                   -5.64215344E+03, 2.66178101E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.32389405E+01, -1.20662335E-02, 2.15309174E-05, -1.14893042E-08, 2.05901892E-12,
                                   -9.43059211E+03, -7.02795064E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.834 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 64,
    label = "HCNX",
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
    label = "XCHXN",
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
    label = "XCHNH",
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
    label = "XCHXNH",
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
    label = "XCHNH2",
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
    label = "XCHO",
    molecule =
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.33925015E+00, 1.56187879E-02, -1.78706053E-05, 1.16103367E-08, -3.20827392E-12,
                                   -2.80401952E+04, -4.27823196E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.47250182E+00, -4.25652358E-03, 7.67240272E-06, -4.15094290E-09, 7.52057428E-13,
                                   -2.96018735E+04, -3.52777491E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.573 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 70,
    label = "XCHXO",
    molecule =
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[8.73097043E-01, 1.93259085E-02, -2.43372823E-05, 1.61326691E-08, -4.34526720E-12,
                                   -2.45575801E+04, -2.94044233E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.63455521E+00, -3.73566071E-03, 6.72665116E-06, -3.63437732E-09, 6.57956785E-13,
                                   -2.62017814E+04, -3.67791287E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.275 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 71,
    label = "XCHOH",
    molecule =
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-5.00706212E-01, 2.03875126E-02, -1.83412371E-05, 8.05213048E-09, -1.17601762E-12,
                                   -2.63039895E+04, 7.42264310E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.40355286E+00, -6.56451064E-03, 1.17183592E-05, -6.25846821E-09, 1.12274887E-12,
                                   -2.86342060E+04, -3.79680665E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.949 eV.

                The two lowest frequencies, 12.0 and 58.4 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 72,
    label = "XCH2XO",
    molecule =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.36104022E-01, 2.26483369E-02, -2.39239155E-05, 1.37256579E-08, -3.24031427E-12,
                                   -2.13985316E+04, -1.88215814E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.52489548E+00, -6.50734050E-03, 1.16586275E-05, -6.25680688E-09, 1.12649338E-12,
                                   -2.37480774E+04, -4.84225553E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.213 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 73,
    label = "XCOOH",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.59051461E-01, 2.50172545E-02, -3.09587526E-05, 2.00287012E-08, -5.26520494E-12,
                                   -5.77319467E+04, 3.52735255E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.16264817E+00, -4.70146235E-03, 8.43555601E-06, -4.53366378E-09, 8.17971447E-13,
                                   -5.98836653E+04, -4.05975157E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.570 eV.

                The two lowest frequencies, 36.7 and 64.6 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 74,
    label = "CO2X",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.00959799E+00, 1.33597565E-02, -1.62303912E-05, 1.10029585E-08, -3.14484723E-12,
                                   -5.27818299E+04, -2.58903014E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.98298591E+00, -3.09871776E-03, 5.62883251E-06, -3.07847525E-09, 5.62449215E-13,
                                   -5.40334894E+04, -2.76481272E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied: kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2.DFT binding energy: -0.062 eV. The two lowest frequencies, 10.8 and 12.0 cm-1, where replaced by the 2D gas model. The heat of formation of CO2 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 75,
    label = "HC(O)XO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.65452420E+00, 1.53991982E-02, -1.01838393E-05, 1.75304050E-09, 5.79614481E-13,
                                   -4.59058194E+04, -1.10811323E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.01836282E+01, -5.48155633E-03, 9.93504720E-06, -5.42476495E-09, 9.90183951E-13,
                                   -4.79885042E+04, -4.99790695E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.902 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 76,
    label = "CH2COX",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.89187265E-01, 2.92112653E-02, -3.68630528E-05, 2.57772068E-08, -7.38835035E-12,
                                   -2.28399999E+04, 3.25846272E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.10991553E+01, -7.40804127E-03, 1.32480136E-05, -7.08463685E-09, 1.27176536E-12,
                                   -2.54605657E+04, -5.03706835E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.619 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 77,
    label = "CH3XCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.23038408E+00, 2.13641887E-02, -1.09879577E-05, -4.08548110E-10, 1.72792683E-12,
                                   -3.59888565E+04, 4.12454379E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.28961233E+01, -1.06029491E-02, 1.89557851E-05, -1.01458960E-08, 1.82293047E-12,
                                   -3.92369382E+04, -5.99543192E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.551 eV.

                The two lowest frequencies, 23.8 and 88.9 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 78,
    label = "XCHCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.25530093E-02, 2.79328122E-02, -3.94277430E-05, 2.93799156E-08, -8.78679074E-12,
                                   -1.60291333E+04, 4.03639097E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.11773004E+00, -5.00204545E-03, 8.99633603E-06, -4.84653933E-09, 8.75265787E-13,
                                   -1.81540388E+04, -4.09365888E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.511 eV.

                The two lowest frequencies, 38.0 and 95.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 79,
    label = "XCCHCH2",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.25479749E+00, 3.76847805E-02, -3.93538492E-05, 2.16708327E-08, -4.77858725E-12,
                                   -2.89947855E+03, 4.10178815E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.39365153E+01, -1.03605118E-02, 1.85207758E-05, -9.90839299E-09, 1.77999302E-12,
                                   -6.77659645E+03, -7.28413395E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.430 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 80,
    label = "XCHCHCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {8,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-5.93007302E-01, 3.57123823E-02, -2.88919470E-05, 1.03540097E-08, -6.87748469E-13,
                                   6.18813075E+03, 4.07112708E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.58597409E+01, -1.28922295E-02, 2.29899230E-05, -1.22606374E-08, 2.19689224E-12,
                                   1.82046544E+03, -8.00996985E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.359 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 81,
    label = "XCHCHCH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.93063496E-01, 2.88384322E-02, -1.13116346E-05, -5.04671551E-09, 4.14390397E-12,
                                   -3.09776091E+03, 4.76068688E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.67774942E+01, -1.57411973E-02, 2.80704427E-05, -1.49721483E-08, 2.68245819E-12,
                                   -7.74608865E+03, -8.12380722E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.944 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 82,
    label = "CH3CHCH2X",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.01283183E+00, 3.96054673E-02, -2.41796124E-05, 3.23567437E-09, 1.99314176E-12,
                                   -1.04789510E+04, 3.34183380E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.95941002E+01, -1.84981215E-02, 3.29579796E-05, -1.75535179E-08, 3.14139881E-12,
                                   -1.61123060E+04, -1.02828351E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.713 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 83,
    label = "XCH2CH2CH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-5.78976324E-01, 3.71915827E-02, -1.22898025E-05, -8.77177071E-09, 6.04039735E-12,
                                   -1.43963383E+04, 1.47277870E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.15363954E+01, -2.15932574E-02, 3.85299240E-05, -2.05691913E-08, 3.68755975E-12,
                                   -2.06392762E+04, -1.13399138E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.333 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 84,
    label = "CH3CH2CH3X",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.15856144E+00, 2.48539972E-02, 1.53525973E-05, -3.25302366E-08, 1.35067652E-11,
                                   -1.91073818E+04, -8.74139325E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.32832355E+01, -2.45407014E-02, 4.37313468E-05, -2.33036993E-08, 4.17150293E-12,
                                   -2.54338716E+04, -1.20201845E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.241 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 85,
    label = "CH2XCCH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.72979307E+00, 4.77487399E-02, -4.57827060E-05, 2.34519012E-08, -4.78486001E-12,
                                   -9.27216894E+03, 9.23470861E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.78566754E+01, -1.57310158E-02, 2.81077398E-05, -1.50276611E-08, 2.69754383E-12,
                                   -1.46254983E+04, -9.54811248E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.195 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 86,
    label = "CH3XCHCH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.40036274E-01, 3.58616425E-02, -1.11021659E-05, -8.97397908E-09, 5.91635074E-12,
                                   -1.50153594E+04, -9.77178836E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.15065179E+01, -2.15386628E-02, 3.84133775E-05, -2.04904605E-08, 3.67103983E-12,
                                   -2.11387596E+04, -1.13463590E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.157 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 87,
    label = "XCH2XCHXCH2",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  X u0 p0 c0 {1,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-3.02780964E+00, 4.86827920E-02, -4.64697726E-05, 2.28751861E-08, -4.23877600E-12,
                                   -9.04793299E+03, 1.15070732E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.77787700E+01, -1.55322169E-02, 2.76898539E-05, -1.47575432E-08, 2.64275606E-12,
                                   -1.44350078E+04, -9.42606313E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.196 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 88,
    label = "XOC(O)XO",
    molecule =
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  O u0 p2 c0 {1,D} 
3  O u0 p2 c0 {1,S} {5,S}
4  O u0 p2 c0 {1,S} {6,S}
5  X u0 p0 c0 {3,S}
6  X u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.60792367E-01, 2.96600289E-02, -3.74624110E-05, 2.35857040E-08, -5.97915120E-12,
                                   -6.29096622E+04, 4.32145289E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.00467898E+01, -3.51638045E-03, 6.49177075E-06, -3.63351445E-09, 6.76297410E-13,
                                   -6.52851340E+04, -4.46692931E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). 
        		Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso 
        		using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) 
        		following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
        		kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
        		fmax=2.5e-2. DFT binding energy: -3.027 eV. 
        		The two lowest frequencies, 89.5 and 92.5 cm-1, where replaced by the 2D gas model. 
        		The heat of formation of CO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 89,
    label = "XOC(OH)O",
    molecule =
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.01328212E+00, 3.26276222E-02, -3.70609785E-05, 2.09604143E-08, -4.66693351E-12,
                                   -7.71489241E+04, -4.75360743E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.28523534E+01, -5.70824836E-03, 1.02858082E-05, -5.56715984E-09, 1.01065309E-12,
                                   -8.01059462E+04, -6.44494097E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298, 'K'),
        Tmax=(2000, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py). Based on DFT calculations by Bjarne Kreitz from Brown University. PAW DFT calculations were performed with Quantum Espresso using the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage) following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF', fmax=2.5e-2. DFT binding energy: -2.365 eV. The heat of formation of HCO3 was corrected by +0.41 eV since the BEEF-vdW functional overestimates the binding energy (see SI of DOI:10.1039/c0ee00071j)""",
    metal="Pt",
    facet="111",
)

entry(
    index = 90,
    label = "HCOOHX",
    molecule =
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.35698005E+00, 1.65817950E-02, -8.93246966E-06, -5.96590960E-10, 1.65711542E-12,
                                   -5.36942403E+04, -5.43199062E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.10477913E+01, -7.24274370E-03, 1.29091018E-05, -6.88021503E-09, 1.23289550E-12,
                                   -5.60975560E+04, -4.54728471E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.216 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 91,
    label = "HCO2CH3X",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.37688850E+00, 1.71682950E-02, 1.02263070E-05, -2.31122378E-08, 9.75945366E-12,
                                   -5.42731237E+04, -7.59071433E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.73815092E+01, -1.48389347E-02, 2.65610657E-05, -1.42501123E-08, 2.56517842E-12,
                                   -5.84957255E+04, -8.16468299E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.318 eV.

                The two lowest frequencies, 62.9 and 75.5 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 92,
    label = "H2C(XO)OCH3",
    molecule =
"""
1 O u0 p2 c0 {2,S} {10,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[1.68079896E+00, 3.12126215E-02, -8.07893400E-06, -1.08377033E-08, 6.48220713E-12,
                                   -4.78005666E+04, -5.80786049E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.04132198E+01, -1.73601838E-02, 3.10764492E-05, -1.66713256E-08, 3.00083064E-12,
                                   -5.31436983E+04, -1.03396841E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.997 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 93,
    label = "H2C(XO)XO",
    molecule =
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 O u0 p2 c0 {2,S} {7,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {5,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.69923804E-01, 2.86585416E-02, -2.78936419E-05, 1.36526428E-08, -2.53912516E-12,
                                   -3.69195622E+04, -3.70031423E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.22233961E+01, -7.74165833E-03, 1.39418350E-05, -7.54192659E-09, 1.36669487E-12,
                                   -4.00006152E+04, -6.06800543E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.554 eV.
    """,
    metal="Pt",
    facet="111",
)


entry(
    index = 94,
    label = "XOCH2CH3",
    molecule =
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.61067651E-01, 2.53309271E-02, -2.95243491E-06, -1.26602001E-08, 6.61140934E-12,
                                   -2.62713434E+04, 3.45861454E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.67501781E+01, -1.61554398E-02, 2.88603109E-05, -1.54358268E-08, 2.77154673E-12,
                                   -3.09596398E+04, -8.15974052E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -1.905 eV.

                The two lowest frequencies, 12.0 and 92.3 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 95,
    label = "XCCCH2",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-3.82821995E-01, 3.18369145E-02, -4.01391269E-05, 2.76197052E-08, -7.78850595E-12,
                                   1.14918022E+04, 5.75967137E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.11180258E+01, -7.40595551E-03, 1.32616442E-05, -7.10517630E-09, 1.27762668E-12,
                                   8.68012627E+03, -5.18344590E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.773 eV.

                The two lowest frequencies, 12.0 and 99.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 96,
    label = "XCXCCH2",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.27103445E+00, 4.27539019E-02, -5.61652527E-05, 3.84419292E-08, -1.06004164E-11,
                                   1.29825200E+04, 6.93062665E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.21290474E+01, -7.57219828E-03, 1.36015955E-05, -7.32089312E-09, 1.32157610E-12,
                                   9.54617923E+03, -6.48251627E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.648 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 97,
    label = "XCCH2CH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-4.07836856E-01, 3.38179738E-02, -1.82365043E-05, -2.17799277E-10, 2.78237156E-12,
                                   -1.53008520E+04, 3.03397088E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.76952935E+01, -1.61873878E-02, 2.89121382E-05, -1.54560860E-08, 2.77424705E-12,
                                   -2.03063191E+04, -9.05055229E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -6.099 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 98,
    label = "XCCH2OH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-4.14367704E-01, 2.97866357E-02, -2.42611023E-05, 8.22145796E-09, -2.81785012E-13,
                                   -2.93330896E+04, 7.21907667E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.30250135E+01, -9.79365971E-03, 1.74609646E-05, -9.31041024E-09, 1.66893053E-12,
                                   -3.28968547E+04, -6.15413406E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.950 eV.

                The two lowest frequencies, 12.0 and 51.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 99,
    label = "XCCHO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.54881082E-01, 2.46650429E-02, -2.78829260E-05, 1.67435167E-08, -4.17255119E-12,
                                   -2.35262603E+04, 5.36194261E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.17648225E+00, -5.39008423E-03, 9.76740931E-06, -5.32718475E-09, 9.71578780E-13,
                                   -2.58913224E+04, -4.17960043E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.377 eV.

                The two lowest frequencies, 20.1 and 76.7 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 100,
    label = "XCCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.82296413E-01, 2.58715605E-02, -3.93603870E-05, 3.04629746E-08, -9.36533490E-12,
                                   -2.01168302E+04, -3.57376015E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.07081859E+00, -3.00851572E-03, 5.51539311E-06, -3.04805549E-09, 5.61469009E-13,
                                   -2.18315109E+04, -4.08625858E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -5.276 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 101,
    label = "CH3CH2XCO",
    molecule =
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {2,S} {10,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {4,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.17980384E-01, 3.37808273E-02, -1.47996341E-05, -3.84914220E-09, 3.93637206E-12,
                                   -3.72200739E+04, 3.57199396E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.93377955E+01, -1.74343755E-02, 3.11976589E-05, -1.67226574E-08, 3.00798191E-12,
                                   -4.25606618E+04, -9.50724091E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.348 eV.

                The two lowest frequencies, 12.0 and 63.5 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 102,
    label = "CH3CH2OHX",
    molecule =
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
10 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.44141648E+00, 2.01418511E-02, 1.00444529E-05, -2.46324618E-08, 1.06436492E-11,
                                   -3.27027814E+04, -2.16253584E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.85992615E+01, -1.79442101E-02, 3.18809278E-05, -1.69157790E-08, 3.01870761E-12,
                                   -3.75006032E+04, -8.72751435E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.023 eV.

                The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 103,
    label = "CH3XCHOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-9.38075627E-02, 3.25418587E-02, -1.95081006E-05, 1.90337747E-09, 2.01784423E-12,
                                   -3.55483318E+04, 5.47743439E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.68236097E+01, -1.50325950E-02, 2.67326715E-05, -1.41983594E-08, 2.53584549E-12,
                                   -4.01702789E+04, -8.16921311E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.332 eV.

                The two lowest frequencies, 12.0 and 96.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 104,
    label = "CH3XCOH",
    molecule =
"""
1 O u0 p2 c0 {3,S} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-2.64775456E-01, 3.03517808E-02, -2.04737999E-05, 4.47036782E-09, 8.49809806E-13,
                                   -3.50990912E+04, 6.53319807E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.48988986E+01, -1.28910736E-02, 2.29998891E-05, -1.22748249E-08, 2.20049375E-12,
                                   -3.92164063E+04, -7.14636815E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.952 eV.

                The two lowest frequencies, 12.0 and 58.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 105,
    label = "XCHCCH2",
    molecule =
"""
1 C u0 p0 c0 {3,D} {4,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {1,S}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.47420628E+00, 4.21450105E-02, -5.01975896E-05, 3.19228373E-08, -8.24990770E-12,
                                   8.41268003E+03, 6.36468208E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.41133329E+01, -9.85218182E-03, 1.76095803E-05, -9.41496495E-09, 1.69037771E-12,
                                   4.56774046E+03, -7.19224209E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -2.423 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 106,
    label = "XCHCH2CH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[-1.60792265E+00, 3.65072698E-02, -1.73028330E-05, -2.63268524E-09, 3.77289172E-12,
                                   -7.88720055E+03, 1.17179700E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.86868441E+01, -1.88617963E-02, 3.36944612E-05, -1.80170490E-08, 3.23426057E-12,
                                   -1.35427152E+04, -9.33401144E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.649 eV.

                The two lowest frequencies, 12.0 and 74.1 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 107,
    label = "CH3XCCH3",
    molecule =
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[4.03765346E-01, 3.43477499E-02, -1.58933907E-05, -2.43971983E-09, 3.40954348E-12,
                                   -1.01231228E+04, -2.81376113E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.97785534E+01, -1.85076861E-02, 3.30425254E-05, -1.76515167E-08, 3.16607226E-12,
                                   -1.55305215E+04, -1.03131111E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -3.420 eV.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 108,
    label = "CH3CHOX",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0
""",
    thermo=NASA(
        polynomials=[
            NASAPolynomial(coeffs=[2.76865237E+00, 1.54209040E-02, 5.76787174E-06, -1.58270365E-08, 6.75180571E-12,
                                   -3.01203013E+04, -5.05938429E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.48477497E+01, -1.33581956E-02, 2.38689301E-05, -1.27693401E-08, 2.29305318E-12,
                                   -3.37162085E+04, -6.86748062E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin=(298.0, 'K'),
        Tmax=(2000.0, 'K'),
    ),
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
                Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
                using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
                following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
                kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
                fmax=2.5e-2. DFT binding energy: -0.259 eV.

                The two lowest frequencies, 30.5 and 72.0 cm-1, where replaced by the 2D gas model.
    """,
    metal="Pt",
    facet="111",
)

entry(
    index = 109,
    label = "CH2CH2X",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[1.30720584E+00, 1.65960781E-02, -1.65593895E-06, -8.53643563E-09, 4.49817961E-12, -4.71848181E+02, 1.00987103E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.21842322E+01, -1.15021314E-02, 2.03950515E-05, -1.07880418E-08, 1.91997845E-12, -3.57155818E+03, -5.56581654E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.216 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "CH3XCHXCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {10,S}
3 C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-2.34433622E+00, 4.52667542E-02, -3.34476860E-05, 1.03612371E-08, -1.30499778E-13, -1.42637112E+04, 8.41335045E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.96554137E+01, -1.86218831E-02, 3.32265550E-05, -1.77334320E-08, 3.17881568E-12, -2.01820853E+04, -1.04466461E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.046 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
    label = "CH2CCH2X",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,D} 
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[3.46550846E-01, 3.32090432E-02, -3.22987737E-05, 1.77521100E-08, -4.03378719E-12, 1.10873669E+04, 3.58666724E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.49403509E+01, -1.22710198E-02, 2.18143728E-05, -1.15729874E-08, 2.06442673E-12, 7.30751447E+03, -7.05497634E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.277 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 112,
    label = "OC(OH)OHX",
    molecule =
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89699352E+00, 3.13653839E-02, -3.45366352E-05, 1.93803790E-08, -4.25074559E-12, -8.12277696E+04, -6.82208145E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.38341567E+01, -7.12667706E-03, 1.26390399E-05, -6.68179574E-09, 1.19065178E-12, -8.42168632E+04, -6.09099445E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.348 eV.

            The two lowest frequencies, 12.0 and 37.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "XCCH2XCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {9,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 X u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.02635101E+00, 5.03308424E-02, -5.38588531E-05, 3.03407703E-08, -6.84918788E-12, -1.83932693E+03, 1.57737894E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.58963681E+01, -1.32662345E-02, 2.37473427E-05, -1.27307691E-08, 2.29051345E-12, -6.89229496E+03, -8.49812453E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.341 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "XCHCH2XC",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,D}
3 C u0 p0 c0 {1,S} {8,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 X u0 p0 c0 {2,D}
8 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.80891778E+00, 5.37146126E-02, -6.67782051E-05, 4.32782810E-08, -1.13023410E-11, 7.47231389E+03, 1.78493803E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.40662167E+01, -1.04801296E-02, 1.88192337E-05, -1.01307240E-08, 1.82883288E-12, 2.88808735E+03, -7.66191987E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.292 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "XCHCHXC",
    molecule =
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.40514908E+00, 4.77243064E-02, -6.43560316E-05, 4.44980067E-08, -1.22960184E-11, 1.06656511E+04, 1.18363424E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.21348559E+01, -7.52689921E-03, 1.35205213E-05, -7.27718880E-09, 1.31382482E-12, 7.01422815E+03, -6.53413425E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.402 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "XCH2CH2XCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3 C u0 p0 c0 {1,S} {8,S} {9,S} {11,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 X u0 p0 c0 {2,S}
11 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.87649194E+00, 5.04109402E-02, -4.03708786E-05, 1.47882509E-08, -1.23971666E-12, -1.08810425E+04, 1.57499252E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.96601200E+01, -1.89254315E-02, 3.38211492E-05, -1.80931479E-08, 3.24941421E-12, -1.71576209E+04, -1.04756688E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.283 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
    label = "XCHCH2XCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
3 C u0 p0 c0 {1,S} {8,S} {10,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
10 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.48448515E+00, 4.96119073E-02, -4.65420230E-05, 2.23779541E-08, -4.03109490E-12, 1.04363794E+03, 1.37505559E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.78868252E+01, -1.58385251E-02, 2.83251785E-05, -1.51673166E-08, 2.72609641E-12, -4.52331062E+03, -9.50346021E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.146 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
    label = "XCXCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,T}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-1.79815684E+00, 3.26996376E-02, -4.25662573E-05, 2.91542676E-08, -8.03585670E-12, -2.41279838E+03, 5.84807669E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[9.43023108E+00, -6.45957592E-03, 1.15448998E-05, -6.16905671E-09, 1.10713611E-12, -5.09639939E+03, -5.01225511E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.916 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "XCH2CHO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.28083316E-01, 2.85783353E-02, -2.22349304E-05, 7.78829612E-09, -5.93358696E-13, -2.61437894E+04, 7.51944172E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.29781551E+01, -1.07278120E-02, 1.92368201E-05, -1.03414540E-08, 1.86454984E-12, -2.97800151E+04, -6.17793029E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.976 eV.

            The two lowest frequencies, 58.8 and 75.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
    label = "XCH2CH2OH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {9,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.94518379E+00, 3.95654165E-02, -3.03930791E-05, 9.79289880E-09, -1.95808647E-13, -3.18718778E+04, 1.31064835E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.67847482E+01, -1.52226559E-02, 2.70968887E-05, -1.44118191E-08, 2.57708191E-12, -3.68744949E+04, -8.28571980E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.488 eV.

            The two lowest frequencies, 12.0 and 93.4 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "XCH2XCOH",
    molecule =
"""
1 O u0 p2 c0 {3,S} {6,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
8 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.37007233E+00, 4.52879213E-02, -5.44419673E-05, 3.43225741E-08, -8.71185762E-12, -2.87351749E+04, 8.33692180E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.40545368E+01, -9.76944446E-03, 1.74383432E-05, -9.30556763E-09, 1.66873012E-12, -3.27602868E+04, -7.40554815E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.361 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
    label = "CH2XCOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.00416383E-01, 3.61961687E-02, -4.28843203E-05, 2.71417157E-08, -6.93485547E-12, -2.27718522E+04, 5.48365659E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.31911025E+01, -8.86429182E-03, 1.57291273E-05, -8.31877139E-09, 1.48112563E-12, -2.60890312E+04, -6.22425505E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -2.837 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "XCHXCO",
    molecule =
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,D}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,D}
6 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-1.37761371E+00, 3.72565997E-02, -5.30168625E-05, 3.85555128E-08, -1.11934628E-11, -2.69771842E+04, 3.96229085E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.01988493E+01, -5.11717278E-03, 9.26394034E-06, -5.03840097E-09, 9.16957643E-13, -2.96506342E+04, -5.32680120E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.460 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
    label = "CH3OCH3X",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
10 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37271709E+00, 1.19486098E-02, 2.71504465E-05, -3.88526285E-08, 1.49405852E-11, -3.14414135E+04, -7.75895151E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.85166607E+01, -1.90746655E-02, 3.40122343E-05, -1.81459402E-08, 3.25144074E-12, -3.61998252E+04, -8.87571696E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.362 eV.

            The two lowest frequencies, 12.0 and 67.3 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
    label = "XCCH2XC",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,T}
3 C u0 p0 c0 {1,S} {7,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 X u0 p0 c0 {2,T}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.54184110E+00, 5.16072922E-02, -6.99489368E-05, 4.85158534E-08, -1.34564929E-11, 1.42819935E+04, 1.65180273E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.21430416E+01, -7.83417928E-03, 1.41226720E-05, -7.64053459E-09, 1.38487512E-12, 1.03648004E+04, -6.63229379E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.613 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 126,
    label = "XCHXCHXCH",
    molecule =
"""
1 C u0 p0 c0 {7,D} {2,S} {4,S}
2 C u0 p0 c0 {8,S} {1,S} {3,S} {5,S}
3 C u0 p0 c0 {9,D} {2,S} {6,S}
4 H u0 p0 c0 {1,S} 
5 H u0 p0 c0 {2,S} 
6 H u0 p0 c0 {3,S} 
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {2,S}
9 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.92854074E+00, 5.53472012E-02, -7.06461759E-05, 4.67854057E-08, -1.24376690E-11, 3.14615034E+03, 1.82810138E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.40834570E+01, -1.02652951E-02, 1.84117274E-05, -9.89306924E-09, 1.78340127E-12, -1.42016228E+03, -7.66281115E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -6.285 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
    label = "XCHCHXCH",
    molecule =
"""
1 C u0 p0 c0 {7,D} {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {8,S} {2,D} {6,S}
4 H u0 p0 c0 {1,S} 
5 H u0 p0 c0 {2,S} 
6 H u0 p0 c0 {3,S} 
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.24543107E+00, 4.57407291E-02, -5.20679215E-05, 3.10116074E-08, -7.43118067E-12, 4.23624859E+03, 1.42275299E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.39737231E+01, -1.05202964E-02, 1.88516802E-05, -1.01204190E-08, 1.82311527E-12, -6.01127146E+01, -7.25198475E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -6.189 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
    label = "XCHXCHCH3",
    molecule =
"""
1 C u0 p0 c0 {9,D} {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {10,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,D}
10 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-2.57393128E+00, 4.77399245E-02, -4.59807447E-05, 2.35135768E-08, -4.74550260E-12, -8.27681577E+03, 9.44154348E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.79080385E+01, -1.55492702E-02, 2.77729619E-05, -1.48415413E-08, 2.66313378E-12, -1.35917048E+04, -9.46976696E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.399 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
    label = "XCH2CHCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.33599764E+00, 4.09549542E-02, -3.30896797E-05, 1.23408962E-08, -1.07948372E-12, -4.13833536E+03, 1.48603663E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.67497477E+01, -1.55450741E-02, 2.76946971E-05, -1.47478624E-08, 2.63918113E-12, -9.20706876E+03, -8.27715317E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.775 eV.

            The two lowest frequencies, 12.0 and 74.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
    label = "XOCHCH2",
    molecule =
"""
1 O u0 p2 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.99354280E-01, 3.62950600E-02, -3.94436193E-05, 2.30734162E-08, -5.50516577E-12, -1.63485919E+04, -5.24288186E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.40890656E+01, -9.90516134E-03, 1.76961471E-05, -9.45700790E-09, 1.69729334E-12, -1.99913758E+04, -7.32427736E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.133 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
    label = "XCHCHXCH2",
    molecule =
"""
1 C u0 p0 c0 {8,S} {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {9,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
    polynomials = [
        NASAPolynomial(coeffs=[-4.00241403E+00, 5.22189088E-02, -5.89122044E-05, 3.51035783E-08, -8.41934161E-12, -2.61054041E+03, 1.50822089E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
        NASAPolynomial(coeffs=[1.59486678E+01, -1.28837296E-02, 2.30283272E-05, -1.23167595E-08, 2.21202132E-12, -7.59500163E+03, -8.54536705E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.131 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 132,
    label = "XCXCO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 X u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.97583218E-01, 2.46743148E-02, -3.70136199E-05, 2.82073318E-08, -8.56860763E-12, -1.93579676E+04, -4.67313316E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.17817550E+00, -2.74871719E-03, 5.05296264E-06, -2.80344383E-09, 5.18025206E-13, -2.10138707E+04, -4.05106752E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.210 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 133,
    label = "CHCCH3X",
    molecule =
"""
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49804316E+00, 2.87614176E-02, -2.68862220E-05, 1.52783281E-08, -3.78230086E-12, 1.24272959E+04, -1.11521746E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.48327083E+01, -1.23703052E-02, 2.19686449E-05, -1.16339578E-08, 2.07217584E-12, 8.93071272E+03, -6.90163887E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.310 eV.

            The two lowest frequencies, 51.8 and 63.4 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 134,
    label = "XCHCXCH",
    molecule =
"""
1 C u0 p0 c0 {2,D} {6,S} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {7,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.25979918E+00, 4.29110764E-02, -6.11256480E-05, 4.48105295E-08, -1.30454814E-11, 1.98276362E+04, 3.52530430E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.22618815E+01, -6.84691121E-03, 1.22478884E-05, -6.54778739E-09, 1.17560614E-12, 1.67224657E+04, -6.32437700E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.349 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 135,
    label = "XCHXCXCH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {6,D} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 C u0 p0 c0 {2,S} {8,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 X u0 p0 c0 {1,D}
7 X u0 p0 c0 {2,D}
8 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.33834725E+00, 5.49356355E-02, -8.04348255E-05, 5.94297575E-08, -1.73391856E-11, 9.30136350E+03, 1.51752797E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.22196206E+01, -7.22560903E-03, 1.29807408E-05, -6.98119810E-09, 1.25948043E-12, 5.56850154E+03, -6.62623300E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.271 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 136,
    label = "XCXCCH3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {7,T} 
2 C u0 p0 c0 {1,S} {8,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S} 
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,T}
8 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.70293757E-01, 2.68182339E-02, -2.11880127E-05, 8.20992815E-09, -1.02776468E-12, 3.40078614E+03, 3.50629321E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.29502839E+01, -1.05538555E-02, 1.88909383E-05, -1.01262169E-08, 1.82152861E-12, -3.86320270E+01, -6.20424122E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.747 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 137,
    label = "XCH2XCCH2",
    molecule =
"""
1 C u0 p0 c0 {2,S} {8,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {9,S} {3,D}
3 C u0 p0 c0 {2,D} {6,S} {7,S} 
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.72746229E+00, 4.91193370E-02, -5.72165653E-05, 3.62071595E-08, -9.37581263E-12, 2.39811903E+02, 9.21506685E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.59653882E+01, -1.26651294E-02, 2.26132980E-05, -1.20712119E-08, 2.16431136E-12, -4.40919182E+03, -8.48332759E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.220 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 138,
    label = "XCXCHCH3",
    molecule =
"""
1 C u0 p0 c0 {8,T} {2,S}
2 C u0 p0 c0 {1,S} {9,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S} 
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,T}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15893067E+00, 3.70424993E-02, -3.12332418E-05, 1.29953202E-08, -1.80175319E-12, -8.31681811E+03, 2.95909204E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.58046677E+01, -1.33934550E-02, 2.39475392E-05, -1.28180432E-08, 2.30318510E-12, -1.28236798E+04, -8.37975104E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.100 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 139,
    label = "XCCHXCH2",
    molecule =
"""
1 C u0 p0 c0 {7,D} {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {8,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {1,D}
8 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.32569037E+00, 5.22761881E-02, -6.52481961E-05, 4.25489345E-08, -1.11793769E-11, 6.37361262E+02, 1.57860707E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.40354949E+01, -1.03288659E-02, 1.85144208E-05, -9.93982041E-09, 1.79062970E-12, -3.81398197E+03, -7.60710085E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.141 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 140,
    label = "XCHXCCH3",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {8,S}
2 C u0 p0 c0 {1,D} {3,S} {9,S}  
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {1,S}
9 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23617363E+00, 3.91193103E-02, -3.59445619E-05, 1.70782620E-08, -3.07130016E-12, -6.07711358E+03, 3.54507519E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.59073613E+01, -1.30485761E-02, 2.33187859E-05, -1.24715428E-08, 2.23950830E-12, -1.05658651E+04, -8.38198234E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.915 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 141,
    label = "CH3OCH2OHX",
    molecule =
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 O u0 p2 c0 {3,S} {10,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35949301E+00, 2.65779090E-02, 4.85435584E-06, -2.33007362E-08, 1.08024076E-11, -5.63318991E+04, -2.72908301E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.12488755E+01, -1.93209268E-02, 3.44158139E-05, -1.83320271E-08, 3.28169374E-12, -6.18637175E+04, -1.01870265E+02], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.459 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 142,
    label = "XCXCHXC",
    molecule =
"""
1 C u0 p0 c0 {5,T} {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {1,T}
6 X u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.96827051E+00, 4.82122603E-02, -7.02038671E-05, 5.07019364E-08, -1.44599541E-11, 1.66025547E+04, 1.40625208E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.02561600E+01, -5.01053573E-03, 9.09120689E-06, -4.95996444E-09, 9.05238271E-13, 1.34002676E+04, -5.59084362E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -5.202 eV.
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 143,
    label = "XCHCXC",
    molecule =
"""
1 C u0 p0 c0 {2,D} {5,S} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {6,D}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,S}
6 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.04831422E-01, 2.83762115E-02, -3.78645327E-05, 2.65441259E-08, -7.54179011E-12, 3.36049840E+04, -4.37180969E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.01968696E+01, -4.92542027E-03, 8.88181864E-06, -4.80548132E-09, 8.71059272E-13, 3.13364765E+04, -5.16653737E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.793 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 144,
    label = "XCHXCXC",
    molecule =
"""
1 C u0 p0 c0 {2,S} {5,D} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {6,D}
3 C u0 p0 c0 {2,S} {7,T}
4 H u0 p0 c0 {1,S}
5 X u0 p0 c0 {1,D}
6 X u0 p0 c0 {2,D}
7 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.84882420E-01, 3.60148185E-02, -5.06524253E-05, 3.62843216E-08, -1.03804604E-11, 2.25861922E+04, 1.66468647E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.02578284E+01, -4.86514372E-03, 8.79773214E-06, -4.77770413E-09, 8.68659255E-13, 1.99824258E+04, -5.39672632E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -4.749 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 145,
    label = "XCHCHO",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {6,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D} 
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.25342098E+00, 3.27302187E-02, -3.75493266E-05, 2.32114742E-08, -5.93083221E-12, -1.89537119E+04, 9.92661471E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.11794819E+01, -7.79813608E-03, 1.40437569E-05, -7.59182897E-09, 1.37483935E-12, -2.20804404E+04, -5.27836731E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.420 eV.

            The two lowest frequencies, 12.0 and 98.6 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 146,
    label = "XCHCHXO",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 X u0 p0 c0 {1,S}
7 X u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.78192366E-01, 3.26656436E-02, -3.48212682E-05, 1.92013520E-08, -4.23029667E-12, -2.36566764E+04, 1.48082726E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.21109589E+01, -7.88891095E-03, 1.41901384E-05, -7.66128189E-09, 1.38633384E-12, -2.69133536E+04, -6.32645953E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -3.816 eV.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 147,
    label = "H2C(OH)OHX",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S} 
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.92629641E+00, 2.39209948E-02, -1.11029110E-05, -3.27472177E-09, 3.46492626E-12, -5.47184077E+04, -7.62359459E-01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.49097254E+01, -1.14976893E-02, 2.03256816E-05, -1.07026073E-08, 1.89947433E-12, -5.82986304E+04, -6.78769969E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -0.341 eV.

            The two lowest frequencies, 12.0 and 12.0 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 148,
    label = "XOCH2OH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S} 
3 O u0 p2 c0 {1,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.07412510E+00, 2.29655848E-02, -1.22605664E-05, -1.24601909E-09, 2.54035334E-12, -4.47916098E+04, 1.02956006E+00], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.30486159E+01, -9.84841705E-03, 1.75672095E-05, -9.37554784E-09, 1.68161712E-12, -4.80975623E+04, -6.08626514E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.593 eV.

            The two lowest frequencies, 42.0 and 64.2 cm-1, where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 149,
    label = "XCHCH2XCH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {8,D}
3 C u0 p0 c0 {1,S} {7,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 X u0 p0 c0 {2,D}
9 X u0 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.87253669E+00, 5.56211271E-02, -6.41174541E-05, 3.90946699E-08, -9.64986424E-12, 5.91492593E+03, 1.84285138E+01], Tmin=(298.0, 'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[1.60332585E+01, -1.30870619E-02, 2.34592896E-05, -1.25997206E-08, 2.27017641E-12, 7.10566828E+02, -8.68123330E+01], Tmin=(1000.0, 'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
    longDesc = u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (file: ThermoPt111.py).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',
            fmax=2.5e-2. DFT binding energy: -1.808 eV.
""",
    metal = "Pt",
    facet = "111",
)