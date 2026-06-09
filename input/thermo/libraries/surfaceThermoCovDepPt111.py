name = "Coverage Dependent Thermo for Pt(111)"
shortDesc = u"thermo with coverage dependence for Pt(111) surface species"
longDesc = u"""
COX coverage dependence as calculated by Jongyoon Bae, Bjarne Kreitz, Andrew A. Peterson, and C. Franklin Goldsmith
Journal of Chemical Information and Modeling 2025 65 (7), 3461-3476
DOI: 10.1021/acs.jcim.4c02167
Polynomial coeffients taken from global minimum Pt Table S3. See Supplemental Material.
"""


entry(
    index = 1,
    label = "X",
    molecule = 
"""
1 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0,0,0,0,0,0.0,0.0], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""library value for a vacant surface site""",
    longDesc = u"""Zeros, by definition.""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 2,
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
