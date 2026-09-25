#!/usr/bin/env python
# encoding: utf-8

name = "SurfaceThermoPt111_covdep"
shortDesc = u"Surface adsorbates on Pt(111) with coverage-dependent thermo"
longDesc = u"""
Surface species adsorbed on Pt(111) with coverage-dependent thermo. The thermochemical
properties of the adsorbates are the same as in surfaceThermoPt111.py with the addition of polynomials 
for the coverage-dependent enthalpy of formation of entropy. 

Details for the enthalpies of formation:
All species are computed with a consistent set of DFT settings in Quantum Espresso. 
The reference species used are: *O, *CO, *NO, *H, *. Silbaugh and Campbell have reported the
heats of formation for these adsorbates with respect to elements in their
standard state at 298 K in https://doi.org/10.1021/acs.jpcc.6b06154. We apply
atomic corrections to get these heats of formation with respect to elements in
their standard state at 0 K as descibed by Ruscic and Bross in
https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/B9780444640871000012
We also correct the heat of formation ot the measured coverage down to 1/9 ML
for *O and *CO, and assume the heat of formation of a bare Pt(111) slab is 0. Our
heats of formation at 0 K are:
    "XCO": -230.9,
    "XH": -32.7,
    "XNO": -20.24,
    'XO': -103.7,
    "Pt": 0,
We then use these species and values as an anchor set to compute the heats
of formation for all adosrbates on Pt(111) as described by Kreitz et al.
https://pubs.rsc.org/en/content/articlelanding/2025/cs/d4cs00768a.
Lastly we correct the heats of formation back to being with respec to the
elements in their standard state at 298 K. This process is automated in
C. Franklin Goldsmith's thermo_kinetics_scripts repository in the
new_workflow folder:
https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

Details for the notation:
Note: X indicates a bond to the surface. It is always on the left hand site of
an atom that is bonded to the surface e.g. XCO it means that C is bonded to
the surface. If the X is on the right hand side and at the end of a label, it
means that this species is physisorbed. 

Details for the coverage effects:
Coverage-dependent corrections to the enthalpy of formation and entropy are described
by polynomial models as a function of adsorbate surface coverage, following the approach
of Bae et al. (https://pubs.acs.org/doi/10.1021/acs.jcim.4c02167).
The order in the coefficients is: [(1st order), (2nd order), (3rd order)]
"""

entry(
    index = 1,
    label = "XCO",
    molecule =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 O  u0  p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4289514345775818, 0.014037445912949231, -2.2117880511546713e-05, 1.7865950156490832e-08, -5.7147862830841945e-12, -34568.84870061009, -7.782662330904809], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.486566622473974, -0.0016811903234556856, 3.0903081182232816e-06, -1.7118686775497669e-09, 3.158649696949356e-13, -35481.550855606365, -27.6788563455022], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence = {
            """
            1 C u0 p0 {2,D} {3,D}
            2 O u0 p2 {1,D}
            3 X u0 p0 {1,D}
            """: {
                'model': 'polynomial',
                'enthalpy-coefficients': [(0.312, 'eV/molecule'), (-0.323, 'eV/molecule'), (0.890, 'eV/molecule')],
                'entropy-coefficients': [(1.11e-4, 'eV/(molecule*K)'), (-6.48e-5, 'eV/(molecule*K)'), (-1.63e-4, 'eV/(molecule*K)')]
            }
        },
    ),
    longDesc = u"""
    Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
    Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

    https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

    DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
    functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
    were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
    smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

    COX coverage dependence calculated by Jongyoon Bae, Bjarne Kreitz, Andrew A. Peterson, and C. Franklin Goldsmith
    Journal of Chemical Information and Modeling 2025 65 (7), 3461-3476
    DOI: 10.1021/acs.jcim.4c02167
    Polynomial coeffients taken from global minimum Pt Table S3. See Supplemental Material.
    """,
    metal = "Pt",
    facet = "111",
)

entry(
    index = 2,
    label = "XCH",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.668054071556987, 0.02906936052545507, -4.8265363884475096e-05, 3.875892627442114e-08, -1.1974939840756911e-11, -2202.5553595330853, 9.729432728113348], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.904296267990244, -0.0026386471764010657, 4.717289404373525e-06, -2.5126685290206794e-09, 4.49659036145192e-13, -3748.807352288421, -26.710780698175974], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence={
            """
            1 X  u0 p0 c0 {2,T}           
            2 C  u0 p0 c0 {1,T} {3,S}     
            3 H  u0 p0 c0 {2,S}           
            """: {'model': 'polynomial', 
                  'enthalpy-coefficients': [(62670, 'J/mol'), (0, 'J/mol'), (0, 'J/mol')],
                  'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]}
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

Coverage dependence based on values in the Supporting Information of "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt"
Jonathan E. Sutton, Paraskevi Panagiotopoulou, Xenophon E. Verykios, and Dionisios G. Vlachos
The Journal of Physical Chemistry C 2013 117 (9), 4691-4706
DOI: 10.1021/jp312593u
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.45723412880679587, 0.02222624102464355, -1.667214371225305e-05, 5.7213606113744865e-09, -3.993230911289944e-13, -11043.637207150816, -2.2732381499886802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.307104591573854, -0.009366253405579311, 1.671500714924329e-05, -8.92182977096838e-09, 1.5993403971733366e-12, -13965.245844046643, -57.941171527260124], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence={
              """
              1 X  u0 p0 c0 {3,T}
              2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
              3 C  u0 p0 c0 {1,T} {2,S}
              4 H  u0 p0 c0 {2,S}
              5 H  u0 p0 c0 {2,S}
              6 H  u0 p0 c0 {2,S}
              """: {'model': 'polynomial',
                    'enthalpy-coefficients': [(62670, 'J/mol'), (0, 'J/mol'), (0, 'J/mol')],
                    'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]},
             """
              1 X  u0 p0 c0 {2,T}
              2 C  u0 p0 c0 {1,T} {3,S}
              3 H  u0 p0 c0 {2,S}
              """: {'model': 'polynomial',
                    'enthalpy-coefficients': [(62670, 'J/mol'), (0, 'J/mol'), (0, 'J/mol')],
                    'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]},
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

Coverage dependence based on values in the Supporting Information of "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt"
Jonathan E. Sutton, Paraskevi Panagiotopoulou, Xenophon E. Verykios, and Dionisios G. Vlachos
The Journal of Physical Chemistry C 2013 117 (9), 4691-4706
DOI: 10.1021/jp312593u
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "XO",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.29447758737461366, 0.014416268368780336, -2.6132274716597896e-05, 2.19005960702076e-08, -6.980197262178007e-12, -13066.562285947317, -0.1994364663449193], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.902441066530188, -0.00033857631003595914, 6.433642615608704e-07, -3.663229139884261e-10, 6.900876877074478e-14, -13654.383053304307, -15.255938164267217], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence = {
            """
	    1 X  u0 p0 c0 {2,D}
	    2 O  u0 p2 c0 {1,D}
            """: {
                'model': 'polynomial',
		'enthalpy-coefficients': [(-0.043,'eV/molecule'), (1.042,'eV/molecule'), (0,'eV/molecule')],
                'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]
            }        
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

XO coverage dependence obtained from "Detailed Microkinetics for the Oxidation of Exhaust Gas Emissions 
through Automated Mechanism Generation" by Bjarne Kreitz, Patrick Lott, Jongyoon Bae, Katrín Blöndal, 
Sofia Angeli, Zachary W. Ulissi, Felix Studt, C. Franklin Goldsmith, and Olaf Deutschmann
ACS Catalysis 2022 12 (18), 11137-11151
DOI: 10.1021/acscatal.2c03378
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2303812875933364, 0.021364197591551247, -1.0987964053318556e-05, -4.0854759822882103e-10, 1.7279200745627597e-12, -32282.401311062615, 0.4124679531891413], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896110212786931, -0.010602930836050555, 1.8955766424558903e-05, -1.014588758269268e-08, 1.8229290835573665e-12, -35530.476320764086, -59.95424168175581], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence={""" 
                      1 C u0 p0 {2,D} {3,D} 
                      2 O u0 p2 {1,D}  
                      3 X u0 p0 {1,D}  
                      """: {'model': 'polynomial', 
                            'enthalpy-coefficients': [(62670, 'J/mol'), (0, 'J/mol'), (0, 'J/mol')], 
                            'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]}
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 23.8 and 88.9,where replaced by the 2D gas model.

Coverage dependence based on values in the Supporting Information of "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt"
Jonathan E. Sutton, Paraskevi Panagiotopoulou, Xenophon E. Verykios, and Dionisios G. Vlachos
The Journal of Physical Chemistry C 2013 117 (9), 4691-4706
DOI: 10.1021/jp312593u
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "XNO",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.861978139702, 0.012267712827676622, -1.7731771898190192e-05, 1.3155375661569419e-08, -3.940110211157303e-12, -6275.99064823019, -9.289679054876098], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.603255701316299, -0.0013940149474614871, 2.573609745219915e-06, -1.4363138871988452e-09, 2.6664790772466233e-13, -7148.294106663131, -27.81226494128604], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
            thermo_coverage_dependence = {
                """
                1 X  u0 p0 c0 {2,S}
                2 N  u0 p1 c0 {1,S} {3,D}
                3 O  u0 p2 c0 {2,D}
                """: {
                    'model': 'polynomial',
                    'enthalpy-coefficients': [(0.102,'eV/molecule'),(0.599,'eV/molecule'),(0,'eV/molecule')],
                    'entropy-coefficients': [(0, 'kJ/(mol*K)'), (0, 'kJ/(mol*K)'), (0, 'kJ/(mol*K)')]
                } 
            }, 
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

XNO coverage dependence based on "Detailed Microkinetics for NOx-Inhibited Hydrocarbon Oxidation 
through Automated Mechanism Generation within Correlated Uncertainty on Pt(111)", under review, 
Kirk Badger, Bjarne Kreitz, Patrick Lott, and C. Franklin Goldsmith
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "XNO2",
    molecule = 
"""
1 X  u0  p0 c0  {2,S}
2 N  u0  p0 c+1  {1,S} {3,D} {4,S}
3 O  u0  p2 c0  {2,D}
4 O  u0  p3 c-1  {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6007879331370871, 0.014704856571844503, -1.4669757091958005e-05, 6.819313569634828e-09, -1.147982283770417e-12, -12610.8227172237, -0.7662797899264149], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295789997642349, -0.0025855481326240684, 4.764103709943176e-06, -2.6619174816996855e-09, 4.947906056262268e-13, -14096.822845174105, -29.782768933213145], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence = {
            """
            1 X  u0  p0 c0  {2,S}
            2 N  u0  p0 c+1  {1,S} {3,D} {4,S}
            3 O  u0  p2 c0  {2,D}
            4 O  u0  p3 c-1  {2,S}
            """: {
                'model': 'polynomial',
                'enthalpy-coefficients': [(2.65,'eV/molecule'), (-14.2,'eV/molecule'), (18.1,'eV/molecule')],
                'entropy-coefficients': [(0, 'kJ/(mol*K)'), (0, 'kJ/(mol*K)'), (0, 'kJ/(mol*K)')]
            }
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 31.35 and 43.35,where replaced by the 2D gas model.

Coverage dependence based on "Detailed Microkinetics for NOx-Inhibited Hydrocarbon Oxidation through 
Automated Mechanism Generation within Correlated Uncertainty on Pt(111)", under review, 
Kirk Badger, Bjarne Kreitz, Patrick Lott, and C. Franklin Goldsmith.
Original 4th-order polynomials were refit to 3rd-order (maximum order compatible with current RMG version). 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[-1.7981611203722376, 0.032699651187770046, -4.2566267050901004e-05, 2.9154268374034755e-08, -8.035869472649143e-12, -981.598852018363, 5.8480974735541835], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.43020619567617, -0.006459541211980741, 1.1544864226387672e-05, -6.169040761124964e-09, 1.107133468924275e-12, -3665.1870318123556, -50.122403724130024], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
        thermo_coverage_dependence = {
            """
            1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
            2 C u0 p0 c0 {1,S} {6,T}
            3 H u0 p0 c0 {1,S}
            4 H u0 p0 c0 {1,S}
            5 X u0 p0 c0 {1,S}
            6 X u0 p0 c0 {2,T}
            """: {
                'model': 'polynomial',
                'enthalpy-coefficients': [(62670, 'J/mol'), (0, 'J/mol'), (0, 'J/mol')], 
                'entropy-coefficients': [(0, 'J/(mol*K)'), (0, 'J/(mol*K)'), (0, 'J/(mol*K)')]
            }
        },
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.

Coverage dependence based on values in the Supporting Information of "Combined DFT, Microkinetic, and Experimental Study of Ethanol Steam Reforming on Pt"
Jonathan E. Sutton, Paraskevi Panagiotopoulou, Xenophon E. Verykios, and Dionisios G. Vlachos
The Journal of Physical Chemistry C 2013 117 (9), 4691-4706
DOI: 10.1021/jp312593u
""",
    metal = "Pt",
    facet = "111",
)
