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

-Updated by Kirk Badger at Brown University in 2026. All existing species are now computed with a consistant set of DFT settings in Quantum espresso.
Additionally, many new nitrogen containing species are added. There are now 74 nitrogen containing adsorbates with up to 5 heavy atoms.
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
            0, 0, 0, 0,
            0, 0, 0], Tmin=(298.0,'K'), Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[
            0, 0, 0,   0,
            0, 0, 0], Tmin=(1000.0,'K'), Tmax=(3000.0, 'K')),
        ],
        Tmin = (298.0, 'K'),
        Tmax = (3000.0, 'K'),
    ),
    metal = "Pt",
    facet = "111",
)
entry(
    index = 2,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0132854616344893, 0.03262761058111659, -3.706095174588158e-05, 2.0960395825783326e-08, -4.666933506314308e-12, -81868.85882088562, -4.7536240621565184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852353543588329, -0.00570824849650918, 1.0285808375407427e-05, -5.567159908424826e-09, 1.0106531022767602e-12, -84825.87912595575, -64.44940816059918], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 3,
    label = "OHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,D}
2 X  u0  p0  c0  {6,S}
3 H  u0  p0  c0  {4,S}
4 O  u0  p2  c0  {3,S} {5,S}
5 C  u0  p0  c0  {1,D} {4,S} {6,S}
6 N  u0  p1  c0  {2,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.05959982061160269, 0.034935604893275844, -4.39855790528056e-05, 2.8727528722406607e-08, -7.522184264363574e-12, -33076.989636418584, -0.9052005642652068], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.072877573168544, -0.00664305462261147, 1.1791965438741197e-05, -6.237700543196466e-09, 1.1116826317998652e-12, -35998.118165602595, -61.5268883603407], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
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
            NASAPolynomial(coeffs=[-1.8779203086664225, 0.028356288698697506, -4.277510879499703e-05, 3.274075934781191e-08, -9.75815608872388e-12, -4150.189397374645, 6.329199424648831], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.669211004920813, -0.004662986852426903, 8.163981923387267e-06, -4.222734018968265e-09, 7.383907972091739e-13, -6025.8158770193395, -35.46553410089453], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "HOOHX",
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
            NASAPolynomial(coeffs=[2.9656085337498914, 0.013397832123679605, -1.3429344690682074e-05, 7.121751881737713e-09, -1.4106285584070122e-12, -25249.608284276284, -6.154667707403931], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.635380049446058, -0.004641489077444636, 8.092564580948746e-06, -4.1676236189663395e-09, 7.263873560942958e-13, -26678.748264344853, -34.81282407199182], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 47.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
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
            NASAPolynomial(coeffs=[1.926298861921214, 0.023920986270762924, -1.1102891365437688e-05, -3.274735343361719e-09, 3.4649297320221706e-12, -54718.40817858188, -0.7623716616782339], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909732388832854, -0.011497699076417572, 2.032569157433714e-05, -1.0702611808126942e-08, 1.8994750772814185e-12, -58298.63329802208, -67.8770367839491], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
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
            NASAPolynomial(coeffs=[-0.2962185933988715, 0.02186181914758953, -2.3841617463750646e-05, 1.4095769583907038e-08, -3.388230668255332e-12, -307.6994456551154, 6.207184485801549], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412928956150449, -0.006234425804480822, 1.1089327437980425e-05, -5.8875786554616106e-09, 1.0512700719032776e-12, -2504.4359079358455, -37.771462079077395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 35.45 and 72.61,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
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
            NASAPolynomial(coeffs=[1.4980461074061682, 0.028761407443681834, -2.688619835613685e-05, 1.5278311802666502e-08, -3.7822904530582235e-12, 12427.295332585782, -1.1152321426024887], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832729154984882, -0.012370334275977175, 2.196867477820534e-05, -1.1633971170730466e-08, 2.0721780580768446e-12, 8930.702474511407, -69.01651034223151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 51.8 and 63.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2137160105042675, 0.012214676187922303, 1.9068675577301113e-05, -2.8645440448763678e-08, 1.1057901122546454e-11, -14755.776916697443, -3.3273316867407114], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869139226341218, -0.01767832977387301, 3.144153037560276e-05, -1.6706168903883034e-08, 2.9833575253225206e-12, -18958.891251179324, -75.91019621235004], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 77.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
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
            NASAPolynomial(coeffs=[0.34655425022431197, 0.03320903146374003, -3.229874644014059e-05, 1.7752091169205867e-08, -4.033794132052293e-12, 11087.36624621632, 3.586650323800802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940337148457722, -0.012271000595976094, 2.1814353103818894e-05, -1.1572978619254032e-08, 2.0644252739308432e-12, 7307.523095772825, -70.54967983272971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
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
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "HXNO",
    molecule = 
"""
1 X  u0  p0 c0  {3,D}
2 H  u0  p0 c0  {3,S}
3 N  u0  p0 c+1  {1,D} {2,S} {4,S}
4 O  u0  p3 c-1  {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2935534672256999, 0.012551181494457475, -1.3054228857275018e-05, 7.661604760904095e-09, -1.9215514596160332e-12, -7757.3847004016925, -0.23897969202122304], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.5168215174433115, -0.0038395553030464496, 6.878336370803954e-06, -3.689005627860506e-09, 6.639624483559064e-13, -9108.922945630238, -26.758424636724342], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 38.5 and 75.09,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "XCHO",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 H  u0  p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3392517506347437, 0.015618782360796482, -1.787059252180066e-05, 1.1610327846079934e-08, -3.20827392430445e-12, -28040.195490164428, -4.278239925919107], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472501868868721, -0.004256523643468286, 7.672402782773906e-06, -4.150942931718123e-09, 7.520574349498309e-13, -29601.872951858884, -35.27774836937108], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.33610634372831166, 0.02264832889133042, -2.392389692851722e-05, 1.372564500933275e-08, -3.2403177363526936e-12, -21398.53204675875, -1.8821696787908078], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.52488862496814, -0.006507330938045106, 1.1658617720730415e-05, -6.256802483730977e-09, 1.1264926555990982e-12, -23748.07283485112, -48.422513251657755], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "XCH",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.6680472878038217, 0.029069338138602956, -4.826533132112092e-05, 3.8758909084069156e-08, -1.197493840199293e-11, -2918.1560238567577, 9.729399453355848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.9042986812595295, -0.0026386505447205592, 4.717292856601354e-06, -2.512670074814904e-09, 4.496592934290092e-13, -4464.407126529149, -26.71079316515238], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[0.339069154341588, 0.01798477612437326, -8.009977251468463e-06, -2.618497985761969e-09, 2.5890609101075768e-12, 3058.7372188175027, 4.1390415779888325], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264107395002439, -0.009024685340635264, 1.603009365697747e-05, -8.501798468860542e-09, 1.5167137091078899e-12, 310.36730215351963, -47.20208075096739], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 57.54 and 70.14,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
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
            NASAPolynomial(coeffs=[1.3072075375182828, 0.01659607225538956, -1.6559253185471037e-06, -8.536445042335518e-09, 4.498179606571284e-12, -471.84852840519807, 1.0098625648933126], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.184232258898184, -0.011502131450414807, 2.039505158252219e-05, -1.0788041807467539e-08, 1.919978455058478e-12, -3571.557608987114, -55.65816457564598], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "XNXNCH3",
    molecule = 
"""
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 N  u0 p1 c0 {2,S} {3,S} {5,S}
5 C  u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H  u0 p0 c0 {5,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9091619785380343, 0.021534813613813434, -9.823249366586295e-06, -2.1902942596023663e-09, 2.4632899886523063e-12, 1683.2835825321708, -8.927485547055522], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.863871656738088, -0.010727742260440263, 1.9186856661479928e-05, -1.0276921509403038e-08, 1.8476574064403995e-12, -1665.4001723372257, -70.900741012967], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "XOXONXO",
    molecule = 
"""
1 X  u0  p0 c0  {4,S}
2 X  u0  p0 c0  {5,S}
3 X  u0  p0 c0  {7,S}
4 O  u0  p2 c0  {1,S} {6,S}
5 O  u0  p2 c0  {2,S} {6,S}
6 N  u0  p1 c0  {4,S} {5,S} {7,S}
7 O  u0  p2 c0  {3,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5500262969193481, 0.030684202469102608, -3.992249753741044e-05, 2.5278303136043825e-08, -6.3331111188613676e-12, -24858.52362005104, 4.895455951409511], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242175297856868, -0.0029122603612644444, 5.392008844105333e-06, -3.031193465863102e-09, 5.661929309593158e-13, -27159.7633257977, -43.40465498004178], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 71.1 and 71.28,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
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
            NASAPolynomial(coeffs=[-1.9451797364169352, 0.03956540242304279, -3.0393046626231364e-05, 9.792876353127494e-09, -1.9579476928655026e-13, -31871.8786791076, 13.10646326346898], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.78477602772791, -0.015222694741328471, 2.7096928465957854e-05, -1.4411836968466e-08, 2.577084860344147e-12, -36874.50848732432, -82.85736005667101], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 93.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.2547936215827744, 0.037684767144248746, -3.935381821535873e-05, 2.1670811364191383e-08, -4.778594187015983e-12, -2899.479333450424, 4.101768954903848], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.936501535466054, -0.010360492624125524, 1.8520756188653936e-05, -9.90838417832083e-09, 1.7799915628090041e-12, -6776.587671986613, -72.84125571769354], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
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
            NASAPolynomial(coeffs=[0.4572393156188715, 0.02222622390780541, -1.667211881452797e-05, 5.721347467744554e-09, -3.993264052759571e-13, -11354.732036975842, -2.2732635829239793], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.307097626709929, -0.009366243699099793, 1.671499718077341e-05, -8.921825295936948e-09, 1.5993396589183105e-12, -14276.335231633235, -57.94112892647167], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 23,
    label = "OHXCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {4,D}
2 H  u0  p0  c0  {3,S}
3 O  u0  p2  c0  {2,S} {4,S}
4 C  u0  p0  c0  {1,D} {3,S} {5,S}
5 N  u0  p1  c0  {4,S} {6,S} {7,S}
6 H  u0  p0  c0  {5,S}
7 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.9101399566489873, 0.03643403579329222, -4.2297554017529666e-05, 2.6415078172539904e-08, -6.695602405848433e-12, -40657.87733933419, 8.346346609316207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.917020687604829, -0.0092665518941809, 1.641641421751263e-05, -8.660235302430652e-09, 1.5391698772991309e-12, -44084.192972752426, -61.19161366687353], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 35.97 and 69.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 24,
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
            NASAPolynomial(coeffs=[-2.370067691833459, 0.045287905228815095, -5.4441930156142054e-05, 3.432254837964767e-08, -8.711850685294564e-12, -28735.175820964676, 8.336898697810568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.054550824009052, -0.009769463971518799, 1.7438363219580855e-05, -9.30557660349684e-09, 1.6687316066184114e-12, -32760.292741144352, -74.05556129305924], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.6079189052290737, 0.03650725681966295, -1.730280304462386e-05, -2.6327059517695602e-09, 3.772884782371477e-12, -7887.201314351103, 11.71795140046801], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686830394336674, -0.018861777121957767, 3.3694441510049684e-05, -1.801704019498555e-08, 3.234259112968891e-12, -13542.706466646492, -93.3400307131864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 74.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
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
            NASAPolynomial(coeffs=[0.1533309386454741, 0.02312968678326665, -3.289590795769531e-05, 2.441141448952092e-08, -7.243664001954642e-12, 3189.720769055102, -1.7896837262996588], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537079417328969, -0.0038577507795309633, 6.934770920070903e-06, -3.733040236094633e-09, 6.7380093000881e-13, 1475.4188075262073, -38.320594459139734], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "NHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 X  u0  p0  c0  {6,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {3,S} {5,D}
5 C  u0  p0  c0  {1,S} {4,D} {6,S}
6 N  u0  p1  c0  {2,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7582967946366366, 0.042026401517499944, -5.600753638515023e-05, 3.825182908222041e-08, -1.0409416384415948e-11, -245.2796502631179, 5.853411567519336], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.077474570473491, -0.006939960216315113, 1.2365235918805114e-05, -6.576528299276142e-09, 1.1767590618301862e-12, -3498.939993659258, -62.89449360450202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5789725109422789, 0.03719156947423711, -1.2289771963968407e-05, -8.771791809048261e-09, 6.040390410078089e-12, -14396.339088078337, 1.4727597507430517], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.536381694217713, -0.02159323821878347, 3.852990432548073e-05, -2.056918248879602e-08, 3.6875582882373026e-12, -20639.267448905986, -113.39905386783853], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "XNXCO",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,S}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 O  u0  p2  c0  {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2626258291795631, 0.023970695898387073, -3.5780696767867036e-05, 2.6941743821084965e-08, -8.087010228141622e-12, -19770.287892659064, -6.660766627246156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.290136763413816, -0.002447954963019431, 4.512500116250858e-06, -2.513110578099106e-09, 4.657872140968094e-13, -21366.384912881033, -41.25295452279153], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
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
            NASAPolynomial(coeffs=[-1.7981534894390012, 0.03269962600516455, -4.2566230420913326e-05, 2.91542490369061e-08, -8.035856702282018e-12, -2412.7990649576946, 5.848060021291731], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.430231182423013, -0.006459576055042201, 1.1544899962243683e-05, -6.169056776575097e-09, 1.1071361163869078e-12, -5096.398278132154, -50.12254953508379], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 31,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.3088563851978815, 0.0283916874007885, -3.0151732071123384e-05, 1.771974951629053e-08, -4.275930304276088e-12, 2579.119962673737, 1.0285424176859035], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.348629912270564, -0.008905560700536734, 1.584616974627966e-05, -8.417565551754216e-09, 1.5032447502223972e-12, -383.88246715495006, -57.93257830829966], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 32,
    label = "CHCHX",
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
            NASAPolynomial(coeffs=[0.472397484259402, 0.027761496719987733, -4.488251024138066e-05, 3.68137619172982e-08, -1.161323814891091e-11, 20536.264271650572, 2.4117785112268493], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532291909983012, -0.004937822379131742, 8.640827527955598e-06, -4.462041957190934e-09, 7.786526296378301e-13, 18825.48961862048, -36.66572094479358], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 90.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
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
            NASAPolynomial(coeffs=[0.880908266679414, 0.018320052300656305, -5.853299352285862e-06, -4.76200059261109e-09, 3.300731216127062e-12, -3412.1204040394937, 1.6988541423802932], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.86272199859298, -0.011203107450698802, 1.9721651219833707e-05, -1.031497658472236e-08, 1.820102655560301e-12, -6472.968074174192, -55.20399403423673], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 78.71,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "OCNHX",
    molecule = 
"""
1 X  u0  p0  c0
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 N  u0  p1  c0  {3,D} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.549649161595254, 0.018460038448502983, -2.4200109760726565e-05, 1.7347497091245413e-08, -5.041828066154608e-12, -27382.339134393987, -4.24776437425156], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.09914564301697, -0.00440018433340282, 7.814540603211383e-06, -4.134669468842997e-09, 7.364144304799385e-13, -28958.38120548026, -36.92102410599301], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 26.05 and 32.19,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.4984127088896, 0.04745052289849407, -6.331779821893876e-05, 4.4144524192894254e-08, -1.2310062691422985e-11, -2722.598895615335, 16.9501903638442], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.436461478905347, -0.009004134479819131, 1.6092821219686652e-05, -8.599486637344516e-09, 1.5431118907086212e-12, -6484.983082662116, -62.25662996993202], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "CH2OX",
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
            NASAPolynomial(coeffs=[4.152110941060885, -0.0005487132048017087, 1.6858930590385225e-05, -1.8335786801037157e-08, 6.296303756148092e-12, -21001.06968021703, -11.442037711879983], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.405124888330336, -0.006902168774863108, 1.2352154347418985e-05, -6.623629623294305e-09, 1.1913644441634286e-12, -22482.14852683915, -34.84179113075547], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 51.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "NH2XCNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 H  u0  p0  c0  {4,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 C  u0  p0  c0  {1,S} {4,S} {6,D}
6 N  u0  p1  c0  {5,D} {7,S}
7 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.7328851297248244, 0.03226341164733199, -3.779587705376396e-05, 2.3986538279409256e-08, -6.161557375428117e-12, -6509.496544899626, 1.3588387160694158], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.000137061023471, -0.00855709104302838, 1.507579874185188e-05, -7.885511119293845e-09, 1.3920669867208742e-12, -9533.101585644055, -60.26006040271306], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.45 and 56.05,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.356981745321052, 0.016581789113467055, -8.93245604193931e-06, -5.966003689946505e-10, 1.6571154171085567e-12, -53694.240668458515, -0.5432075164117869], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.04779135974607, -0.007242743771743657, 1.2909101836650357e-05, -6.880215062637572e-09, 1.2328955029475026e-12, -56097.55547689846, -45.472846353414454], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.0573783465802915, 0.012862428884006407, 4.84928695038375e-06, -1.3599718395029272e-08, 5.96899960014774e-12, -31062.132411292885, -12.435908461234026], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113485534322619, -0.011408786775686736, 2.0203001135172224e-05, -1.0664783232591535e-08, 1.8954587248723453e-12, -34019.56211300582, -65.26660390806612], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "XCXC",
    molecule = 
"""
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.25761672253846946, 0.019381161206708936, -2.9969201901782745e-05, 2.2777218830822605e-08, -6.826799542336559e-12, 24931.83065114203, -2.704206528801257], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608145428430299, -0.001423773475814122, 2.641982059575953e-06, -1.482898706580994e-09, 2.765400103395678e-13, 23757.73610654117, -28.85413578279513], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
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
            NASAPolynomial(coeffs=[-3.9682655700924263, 0.04821224322916436, -7.020382754527549e-05, 5.070190901773966e-08, -1.4459940189670561e-11, 16602.55363581829, 14.06249620531019], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.25618784819828, -0.005010574566594026, 9.09124673541548e-06, -4.959982299338515e-09, 9.052412241843371e-13, 13400.254235008359, -55.90859791121436], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "XCHXC",
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
            NASAPolynomial(coeffs=[-0.5903493375056066, 0.02820293094982219, -4.3192054719588326e-05, 3.320670015772697e-08, -1.0016171919646766e-11, 14562.239211536966, 0.22475283272964264], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.5929913939688, -0.003510020572438653, 6.291002447877343e-06, -3.3685290767535198e-09, 6.056109381544889e-13, 12760.47258909763, -39.79604200258437], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "NH2XCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {5,D}
2 H  u0  p0  c0  {4,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 C  u0  p0  c0  {1,D} {4,S} {6,S}
6 N  u0  p1  c0  {5,S} {7,S} {8,S}
7 H  u0  p0  c0  {6,S}
8 H  u0  p0  c0  {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.44426315342025297, 0.035143393541917915, -3.825191195703062e-05, 2.319547565822575e-08, -5.754598186857862e-12, -18549.563336353538, 1.9827666071889034], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.74514219361069, -0.01113296971728403, 1.9585112575923382e-05, -1.022169767857312e-08, 1.8010348359985117e-12, -22148.10219496589, -70.19620556082776], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12.72 and 84.97,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "XOOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.725344253463979, 0.014265170184759477, -2.2141020445308363e-05, 1.7159763247973412e-08, -5.148140594379846e-12, -15933.006904782831, -5.880073500148141], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853407080304272, -0.0020628219096885067, 3.5777124521888544e-06, -1.8218841229896744e-09, 3.147031466937131e-13, -16817.14155570548, -25.965590783472088], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "NHCNHX",
    molecule = 
"""
1 X  u0  p0  c0
2 H  u0  p0  c0  {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 C  u0  p0  c0  {3,D} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8461597506391261, 0.030516767779180953, -4.188170241751797e-05, 3.038456998083873e-08, -8.772416820734819e-12, 2231.440038417888, 1.700598484390028], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071582906242801, -0.006359525728146733, 1.1223991720427978e-05, -5.882504318359561e-09, 1.0398336922415319e-12, -153.41593729962733, -48.97471372204738], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 24.23 and 51.07,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 46,
    label = "NH2NCH3CH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {6,S} {7,S} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 C  u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5 C  u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9579364986986095, 0.03417770159679381, 2.826760350589623e-06, -2.457700198169472e-08, 1.1560079282713076e-11, -5645.6886912674945, 2.110336297847528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884358222017116, -0.025217745838261856, 4.4913423110741845e-05, -2.3913113116198802e-08, 4.2785533688020905e-12, -12612.941317367357, -123.21632842360013], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.85 and 59.82,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 47,
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
            NASAPolynomial(coeffs=[0.5564428527368741, 0.024881884193241183, -3.1883879797680434e-05, 2.1907620558739207e-08, -6.062372825965667e-12, 5310.137587876049, -4.09640099470948], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380929521863289, -0.005719366556090383, 1.0097890187526818e-05, -5.296771085574308e-09, 9.37012913345748e-13, 3193.5737282290975, -48.125145497670374], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.46107024748277925, 0.025330918143713778, -2.95241411134256e-06, -1.2660214463929042e-08, 6.611412806112327e-12, -26271.343964961365, 3.458601622411173], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.75018505264351, -0.016155449576488578, 2.886032092240437e-05, -1.5435831253719646e-08, 2.771547477197628e-12, -30959.642658039298, -81.5974450307295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 92.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3699267416865255, 0.028658531388564657, -2.7893618373901115e-05, 1.3652626507646608e-08, -2.5391216906811565e-12, -36919.56280137152, -0.370046041484299], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223403098656842, -0.007741668107278932, 1.3941845053627606e-05, -7.541931084030117e-09, 1.3666956123401224e-12, -40000.61794894802, -60.680093933753156], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
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
            NASAPolynomial(coeffs=[1.5846760207902084, 0.021387549509509458, -2.6680149499382863e-05, 1.8085986641749082e-08, -4.954679028168485e-12, -10565.28251036238, -8.566494007825689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.406551623095396, -0.005399648922306131, 9.490951838389342e-06, -4.944506127843228e-09, 8.7003523316202e-13, -12457.912335885198, -47.67579637039664], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "XNXCOH",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,D}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,D} {3,S} {5,S}
5 O  u0  p2  c0  {4,S} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2803857910420373, 0.026146381291558756, -3.3204709331127583e-05, 2.1735482177742986e-08, -5.739485275935152e-12, -21772.11060282459, -6.266983747164432], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200444140595133, -0.004387993684222539, 7.853858549677602e-06, -4.205155301682368e-09, 7.569009489132158e-13, -23925.2886332021, -50.85669026114345], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
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
            NASAPolynomial(coeffs=[0.687367474126204, 0.021323469448902975, -2.336039976055324e-05, 1.4597549431102648e-08, -3.8509542776843375e-12, 2360.5220779663437, -4.107463299522058], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.374615944582363, -0.0066065430484157075, 1.1797360181945044e-05, -6.297363597977766e-09, 1.1289628357603193e-12, 146.7713765846038, -48.04572552374324], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
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
            NASAPolynomial(coeffs=[-2.7274572524717122, 0.04911931955016374, -5.721652497603537e-05, 3.62071316553514e-08, -9.375812626277735e-12, 239.81087534852827, 9.21504180455984], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965388395063554, -0.012665129565738375, 2.261329816229308e-05, -1.2071212014237589e-08, 2.164311373349659e-12, -4409.190142873391, -84.83327362637277], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "XNXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,S}
3 N  u0  p1  c0  {1,D} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.14057965370883882, 0.03395928839141774, -4.877970542687829e-05, 3.545524730076265e-08, -1.0228443092508144e-11, 8534.390077477394, -0.9856796655624303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.244757631333274, -0.0044230054762681255, 7.940488035408964e-06, -4.265902533836407e-09, 7.694698624474174e-13, 6164.173439841121, -52.21194594431905], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "XCCHO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,T}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.15487855368882772, 0.02466503412850334, -2.7882905742974466e-05, 1.67435027549696e-08, -4.172544254554822e-12, -23526.260775943676, 5.361930025591014], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176496183301216, -0.005390103654173492, 9.767429234625479e-06, -5.327193686576743e-09, 9.715802550783626e-13, -25891.32907233534, -41.79608509369516], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 20.1 and 76.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "XCOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.28139503852560294, 0.023606090400724623, -3.329587349814532e-05, 2.359374470300372e-08, -6.599876894997081e-12, -30449.908467381625, -2.84939166435208], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.572784026138338, -0.003165794452503801, 5.618129387791434e-06, -2.968323943805841e-09, 5.286847314914158e-13, -32111.88448728771, -38.82975654873838], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 57,
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
            NASAPolynomial(coeffs=[0.8975857479384713, 0.02467430605223327, -3.701359961395603e-05, 2.8207317800893548e-08, -8.568604159542303e-12, -19357.968078290447, -4.673145748543366], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.178182501682011, -0.0027487269566934865, 5.052972658860588e-06, -2.8034483246861914e-09, 5.180259484040403e-13, -21013.87357537048, -40.51071502096373], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.6808021563044655, 0.031212610386516765, -8.0789083685967e-06, -1.0837720993507388e-08, 6.482207132174622e-12, -47800.56722432693, -5.80787639926811], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413219942559014, -0.01736018391676655, 3.107644929253564e-05, -1.667132564139086e-08, 3.0008306359545142e-12, -53143.69728476904, -103.39683977096684], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "ONOHX",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 O  u0 p2 c0 {3,S} {5,S}
5 H  u0 p0 c0 {4,S}


""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.035651661290625, 0.02403762635148776, -3.10715175028547e-05, 2.1274644888654494e-08, -5.936341695989e-12, -26215.141661720365, 0.8423300649336412], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.320902420594948, -0.004524709457421657, 8.146698589352583e-06, -4.39895746622928e-09, 7.961296162925903e-13, -28220.056887707782, -40.56217721897826], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 29.74 and 57.23,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
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
            NASAPolynomial(coeffs=[1.5632792211806477, 0.014266187393854, -1.2973938191255383e-05, 7.2687754684802e-09, -1.690748235860795e-12, -15232.901414920616, -4.452608283390505], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417075986305159, -0.007111062744209318, 1.2402765963078194e-05, -6.388062948060308e-09, 1.112839399284942e-12, -17003.48241868535, -39.25667844445977], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "XCN",
    molecule = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,T}
3 N  u0  p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7671511680188914, 0.004179530413204547, -5.16460306174389e-06, 4.281737107517529e-09, -1.53270538622019e-12, 6753.825835406005, -16.448669925442786], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522345399046397, -0.0014872471506000141, 2.7115514303087297e-06, -1.4880483774407132e-09, 2.725089394624866e-13, 6288.039061699597, -25.372463575785044], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
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
            NASAPolynomial(coeffs=[0.5872272419093946, 0.021884253745618573, -9.092097282359689e-06, -3.2013094266308145e-09, 2.9345692542648294e-12, -5750.2016498455605, -3.0977389241107636], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083489072067747, -0.011983006093140706, 2.1302955374565833e-05, -1.1309817688692583e-08, 2.0190228680020024e-12, -9234.28143683144, -67.81740135471398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "XNHCHO",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 H  u0  p0  c0  {3,S}
3 N  u0  p1  c0  {1,S} {2,S} {5,S}
4 H  u0  p0  c0  {5,S}
5 C  u0  p0  c0  {3,S} {4,S} {6,D}
6 O  u0  p2  c0  {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.5697224109377661, 0.026888160051806834, -2.5056254060616507e-05, 1.1463352656729904e-08, -1.8672528800944832e-12, -32910.505177377694, -3.3542668371249977], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974057020690037, -0.007721493775440698, 1.3817688459358648e-05, -7.405228719062684e-09, 1.3327051932182123e-12, -35890.83998421231, -61.47039926672395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "XCHOH",
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
            NASAPolynomial(coeffs=[-0.5007041222485064, 0.020387505380996075, -1.8341220404454415e-05, 8.052118908019455e-09, -1.1760176166220049e-12, -26303.989925557915, 7.4226327062441815], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.403552916321377, -0.006564510724457786, 1.1718359325497268e-05, -6.258468246674575e-09, 1.1227488750043197e-12, -28634.20533103652, -37.968065521548], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 58.4,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
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
            NASAPolynomial(coeffs=[0.1702965064381586, 0.026818224391284964, -2.1187990710913625e-05, 8.209912931753756e-09, -1.027764678918075e-12, 3400.785577617343, 4.199426716437015], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950283973573839, -0.010553855620259525, 1.8890938379933674e-05, -1.0126216905412885e-08, 1.821528611810081e-12, -38.63111288249456, -61.349263752500676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.158563986374605, 0.024853988358157476, 1.5352617703198102e-05, -3.2530250732843954e-08, 1.350676862021949e-11, -19107.382351837034, -8.741405924676677], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.28324248920475, -0.024540711211524024, 4.373135677424616e-05, -2.3303703808340938e-08, 4.171503691519779e-12, -25433.874505561587, -120.20188474457066], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.7297881782361464, 0.0477487229679998, -4.578266674370648e-05, 2.3451874122656707e-08, -4.784866947105115e-12, -9272.169931404913, 9.234684278219188], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.85666165260097, -0.01573099663032726, 2.8107720156277172e-05, -1.5027652331556597e-08, 2.6975423746144773e-12, -14625.489180530314, -95.4810405802704], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
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
            NASAPolynomial(coeffs=[-3.876486774098759, 0.05041092235724704, -4.037083717101258e-05, 1.4788222259221832e-08, -1.2397097237659693e-12, -10881.04354330642, 15.749899480627548], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.66013395149451, -0.018925451027068645, 3.3821169214707656e-05, -1.8093156895228588e-08, 3.249415703686625e-12, -17157.62666885984, -104.75676803324718], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
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
            NASAPolynomial(coeffs=[3.372718318131053, 0.011948605519731134, 2.7150456278172206e-05, -3.885263527850272e-08, 1.494058696205336e-11, -31441.413724491013, -7.758957601829563], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516664160343957, -0.019074670417355798, 3.401223935596512e-05, -1.8145942414685825e-08, 3.2514411153175722e-12, -36199.82667069849, -88.75718953272656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 67.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "OHXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {4,S}
2 H  u0  p0  c0  {3,S}
3 O  u0  p2  c0  {2,S} {4,S}
4 C  u0  p0  c0  {1,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2535897313874391, 0.0331664250530545, -4.263532659067634e-05, 2.860999415456707e-08, -7.693949644060893e-12, -27088.19814426194, 5.808089455489748], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.171441927115158, -0.00647197678082797, 1.1485655604529038e-05, -6.0731342014698865e-09, 1.0815666921505608e-12, -29818.677462458145, -51.16815885849702], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 15.1 and 62.25,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
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
            NASAPolynomial(coeffs=[-2.3443315809312595, 0.04526673811325242, -3.3447648876703874e-05, 1.0361211371484028e-08, -1.3049283875687934e-13, -14263.712117047095, 8.413327357263116], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.655427687564014, -0.018621902641565248, 3.322657498803786e-05, -1.773344101340974e-08, 3.1788171677175556e-12, -20182.09120145222, -104.46654041689519], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "XCH2",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2300645782186788, 0.029222282416047938, -4.3315468288874015e-05, 3.31428027291935e-08, -9.964716551902342e-12, -222.25659675429264, 8.30171716264823], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834592696160247, -0.0051492538511714245, 9.154900439151632e-06, -4.849169380135208e-09, 8.637658222411613e-13, -2258.972094361942, -36.22149496382639], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 73,
    label = "XCHCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.04255587293465304, 0.027932802284313885, -3.942772006846711e-05, 2.937989976562643e-08, -8.786783800562858e-12, -16029.13393282874, 4.036376718408254], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117743977532806, -0.005002064890272754, 8.996355973457415e-06, -4.846548272764188e-09, 8.752672658917174e-13, -18154.04533446834, -40.93666941907792], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 38.0 and 95.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
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
            NASAPolynomial(coeffs=[-0.9848787280247717, 0.03601480571258881, -5.06523957248035e-05, 3.6284301142324924e-08, -1.0380460380154943e-11, 22586.191460108665, 1.6646681085462038], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.257828530267187, -0.004865143870387635, 8.797732294992285e-06, -4.777704201738108e-09, 8.686592687967868e-13, 19982.427059598413, -53.96726152944254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
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
            NASAPolynomial(coeffs=[0.4987424599124593, 0.020575187483968613, -1.268778417935204e-05, 2.0580096976730705e-09, 8.05244759760626e-13, -5253.700069661373, -3.116375604882025], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.222901125746136, -0.009612809130542856, 1.715947768608812e-05, -9.163517606100242e-09, 1.6433481467715682e-12, -8195.186568178231, -58.400890305140216], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "XNNO",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p1  c0  {1,D} {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.366216905242251, 0.019020740681499365, -2.6531517990758787e-05, 1.9018956406066634e-08, -5.525649382498443e-12, -1128.3064862242904, -10.66468490521628], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334160815533311, -0.002320012120532959, 4.273612948512938e-06, -2.380222376156985e-09, 4.4120735219471815e-13, -2537.827626639155, -40.31024821340094], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "XNHXCO",
    molecule = 
"""
1 X  u0  p0  c0  {4,S}
2 X  u0  p0  c0  {5,S}
3 H  u0  p0  c0  {4,S}
4 N  u0  p1  c0  {1,S} {3,S} {5,S}
5 C  u0  p0  c0  {2,S} {4,S} {6,D}
6 O  u0  p2  c0  {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.671760911419438, 0.024196095571897572, -3.0224106307781846e-05, 1.9895399940588105e-08, -5.340183156787859e-12, -28756.776841997707, -7.690276919546048], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.180364931491424, -0.004638309918568294, 8.319844328464815e-06, -4.468746102314158e-09, 8.058137202616262e-13, -30834.324526936645, -50.31831828858603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 78,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.19306645245111803, 0.028838421998994525, -1.1311610948254996e-05, -5.046731874152569e-09, 4.143907439413397e-12, -3097.7615109628305, 4.760672174748043], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.77750123732734, -0.015741207057722553, 2.807045276052443e-05, -1.4972152812116074e-08, 2.6824589404383318e-12, -7746.091402787762, -81.23811178635668], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 79,
    label = "XO",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.2944742231310568, 0.01441625726654529, -2.6132258567565067e-05, 2.1900587545061747e-08, -6.98019593514676e-12, -16461.923737947396, -0.1994529693939322], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.9024434885594417, -0.0003385796875714501, 6.433677259569432e-07, -3.663244667788907e-10, 6.90090255981083e-14, -17049.744726275676, -15.255951597679068], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
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
            NASAPolynomial(coeffs=[1.230386273235039, 0.021364181138588848, -1.0987940121250096e-05, -4.0856023207660433e-10, 1.727923359950978e-12, -35988.856920165126, 0.4124434938860766], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896116437024084, -0.010602939524945506, 1.8955775325381663e-05, -1.0145891565618452e-08, 1.822929746606375e-12, -39236.9336783432, -59.954277173473585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
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
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "XC",
    molecule = 
"""
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.9435071260361403, 0.019776732831383256, -3.36336478120767e-05, 2.6902708865759773e-08, -8.279588820103712e-12, 7000.565263027651, 7.174688997290197], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134783548688582, -0.0006939614447037248, 1.3030892875136078e-06, -7.387048270359094e-10, 1.387965682836422e-13, 6060.024232490823, -15.573868627012471], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "CO2X",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0095993625509263, 0.013359751800887295, -1.623038022297421e-05, 1.100295092154081e-08, -3.144848964575786e-12, -57517.98198599049, -2.592942043349627], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982982484199035, -0.003098712991854859, 5.6288276125419164e-06, -3.0784730588189656e-09, 5.624488513619069e-13, -58769.638891203824, -27.652011141862076], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 10.8 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "H2X",
    molecule = 
"""
1 X  u0 p0 c0
2 H  u0 p0 c0 {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8640642056131584, 0.0007534561819428265, -1.6557138003720825e-06, 1.5522317389958574e-09, -4.4678204278586486e-13, -1689.2750632157577, -8.858065697537338], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068796960213998, -0.0004958073404741864, 6.59234957641556e-07, -1.7259799397596298e-10, 7.629699988490827e-15, -1700.7005579245533, -9.719180011871295], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "ONNCH3CH3X",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 N  u0 p1 c0 {3,S} {5,S} {6,S}
5 C  u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6 C  u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {5,S}
9 H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9971693162720885, 0.025096348548238535, 1.3274009383360151e-05, -3.229249144943194e-08, 1.3906143597752774e-11, -11839.803439098605, -7.72206159144363], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.931485047682692, -0.02091595534142395, 3.7374058428816125e-05, -2.0002140984265296e-08, 3.5937322453820364e-12, -17811.422253314136, -112.9798376013536], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 41.92 and 44.79,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "XOXO",
    molecule = 
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2231473848521273, 0.01834144566779012, -3.0386319971186215e-05, 2.389158299096169e-08, -7.2681374807537225e-12, -14365.310689946078, -5.827738139972117], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.79295813597036, -0.0007752791096293597, 1.450705044353639e-06, -8.206173954346829e-10, 1.5395191640404254e-13, -15295.468507033649, -27.814782430799514], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "CH3NXNOH",
    molecule = 
"""
1 X  u0  p0  c0  {7,D}
2 N  u0  p2  c-1  {3,S} {7,S}
3 C  u0  p0  c0  {2,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p0  c+1  {1,D} {2,S} {8,S}
8 O  u0  p2  c0  {7,S} {9,S}
9 H  u0  p0  c0  {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.2298280105896993, 0.02857061603848079, -1.4963298962563756e-05, -5.176313642584092e-10, 2.3810120541867263e-12, -9878.916080484803, -3.88141499699622], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.662163695275716, -0.013767034996296631, 2.461032395965204e-05, -1.3171447002254381e-08, 2.3665201200583075e-12, -14167.281592196032, -83.71181218671018], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 11.99 and 57.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 87,
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
            NASAPolynomial(coeffs=[1.3799318568768906, 0.01775103470413556, -1.2084989762157814e-05, 2.539138091112652e-09, 6.810073338581191e-13, -16022.531337723749, -0.28277495203800207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249400879119277, -0.00793852051711074, 1.394200430491105e-05, -7.2651932040060965e-09, 1.2784307609119226e-12, -18391.289299997014, -45.75608364954671], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 21.45 and 69.68,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.6719194973911855, 0.03806450613181091, -3.824359770062638e-05, 2.040231059078257e-08, -4.289291144488061e-12, -8535.33961281254, 10.50407379541928], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.228995066113947, -0.011870659656779477, 2.115216565464864e-05, -1.1264162101025237e-08, 2.0156694171299776e-12, -12611.633006485812, -70.11901785345958], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "OCHNH2X",
    molecule = 
"""
1 X  u0  p0  c0
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {2,D} {4,S} {5,S}
4 H  u0  p0  c0  {3,S}
5 N  u0  p1  c0  {3,S} {6,S} {7,S}
6 H  u0  p0  c0  {5,S}
7 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.969587403874247, 0.02052289466273032, -1.1621280547621207e-05, 6.215825757615234e-10, 1.3989989722240637e-12, -36064.47881397024, -2.3548372776887767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866079481005135, -0.00980042385656314, 1.7404572637224417e-05, -9.22325533388852e-09, 1.6448101391910563e-12, -39062.548782383834, -58.5945861741978], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 29.77 and 83.13,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 90,
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
            NASAPolynomial(coeffs=[-4.928535066156786, 0.05534718152841105, -7.064613041223017e-05, 4.67853742667796e-08, -1.2437668950315839e-11, 3146.149184995358, 18.28098562868972], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083457114456088, -0.010265295379669075, 1.8411727682574056e-05, -9.893069344811372e-09, 1.7834012939381763e-12, -1420.1603857985847, -76.62810888409447], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "XCHXO",
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
            NASAPolynomial(coeffs=[0.8730990245546361, 0.019325901636389226, -2.4337266409277266e-05, 1.6132658100797165e-08, -4.345260262716977e-12, -24557.58055052394, -2.940452198061079], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634569118474064, -0.003735680111357191, 6.726671065437476e-06, -3.6343862440460883e-09, 6.579582612385249e-13, -26201.78821405536, -36.779209771998254], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
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
            NASAPolynomial(coeffs=[2.0573699775793095, 0.01878551011043775, -2.938069724351587e-05, 2.350186851777543e-08, -7.340232588415319e-12, -2449.4025664502924, -10.421554931384392], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609523066033134, -0.0029859167584867937, 5.278299518393383e-06, -2.767395024338096e-09, 4.893079722596751e-13, -3667.433367684879, -37.533505209362595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 93,
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
            NASAPolynomial(coeffs=[-4.325685008569402, 0.05227616954992133, -6.524815321269459e-05, 4.254890479161197e-08, -1.1179376868675206e-11, 637.3601674709355, 15.78604404581501], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035495081023502, -0.010328866072734963, 1.8514421035613457e-05, -9.939820509563878e-09, 1.7906297172559822e-12, -3813.98018545545, -76.07100602733398], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 94,
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
            NASAPolynomial(coeffs=[-4.3383416228785405, 0.05493561603944398, -8.04347803491962e-05, 5.94297263297502e-08, -1.7339199520627346e-11, 9301.36235575865, 15.175251696241196], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.21959304626652, -0.007225570624319904, 1.2980701378227055e-05, -6.981180433014081e-09, 1.259477509332513e-12, 5568.518394053544, -66.26216346010321], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8549618970361985, -0.005541347878692846, 3.0119805912452307e-05, -2.992258851269603e-08, 1.0050251429694068e-11, -11709.627636631374, -9.256206302347813], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.541393766552916, -0.010402513409078933, 1.8377739993644713e-05, -9.667651291471074e-09, 1.712113788146074e-12, -13447.561545015824, -35.56384362882349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.029643429257797, 0.03056436481280869, -2.5733365236408553e-05, 1.1293796508562125e-08, -1.821806594470843e-12, -5642.154087788169, 2.6617654177208347], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.238954399490348, -0.012066252955546966, 2.153093734988074e-05, -1.1489313129942497e-08, 2.059020397351995e-12, -9430.598549859993, -70.27958695073038], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "HC(O)XO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6545257813847285, 0.015399192759007823, -1.0183826670136605e-05, 1.753031763371618e-09, 5.796144814107507e-13, -45905.81976174763, -11.081140115163407], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183628262656756, -0.0054815563934807335, 9.935047271124395e-06, -5.4247649800572645e-09, 9.901839547951652e-13, -47988.503689348705, -49.97906879817951], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.26477234399100147, 0.03035176999255425, -2.0473774973403015e-05, 4.470350596539826e-09, 8.498098058584702e-13, -35099.091809495476, 6.5331825956055], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898898669499161, -0.012891073692233341, 2.2999889257501197e-05, -1.2274824918481617e-08, 2.2004937612731326e-12, -39216.40530322082, -71.46368014442395], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 58.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
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
            NASAPolynomial(coeffs=[-1.2534176212234847, 0.03273020710355643, -3.754929968340677e-05, 2.321145562250547e-08, -5.930839153123202e-12, -18953.71259902118, 9.926598033908668], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179468174879117, -0.00779811690179576, 1.4043737251600803e-05, -7.591820150798237e-09, 1.3748378944225233e-12, -22080.43183696676, -52.78358959003789], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 98.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
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
            NASAPolynomial(coeffs=[-1.1589268706614568, 0.03704248615588869, -3.1233211398208106e-05, 1.2995299183184974e-08, -1.8017601299824548e-12, -8316.818879934128, 2.9590731669920447], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.804653938713914, -0.013393435838752776, 2.3947519559819504e-05, -1.2818034367726568e-08, 2.3031836481675772e-12, -12823.671045900091, -83.79742663135006], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "XCNO",
    molecule = 
"""
1 X  u0  p0  c0  {2,T}
2 C  u0  p0  c0  {1,T}, {3,S}
3 N  u0  p1  c0  {2,S} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3606845113620176, 0.014165730210107362, -1.8920019008514142e-05, 1.3801126624201276e-08, -4.17869384927716e-12, -3139.0683951853784, -5.69574266490236], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.213817876105713, -0.0025695804418745093, 4.7049065756329745e-06, -2.59884802643941e-09, 4.785325044545847e-13, -4330.973236740023, -29.994800796459366], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 67.9 and 67.9,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
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
            NASAPolynomial(coeffs=[0.9288946551072278, 0.016318625808529733, 6.612725716932379e-06, -1.7902849148795664e-08, 7.848204724991703e-12, -16071.234276619762, 1.6939762269788439], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774420011612554, -0.014595529984813184, 2.584779947691287e-05, -1.3646600194900631e-08, 2.4255124479537725e-12, -19850.89677284663, -65.80622703440591], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 95.95,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "XNNH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.1312884557033114, 0.018402865797038696, -2.427788191413619e-05, 1.7224355907441603e-08, -4.970784200919454e-12, 10362.914692213575, -5.779521623383209], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494137250133281, -0.003797247762429778, 6.797288946156097e-06, -3.6381823616072336e-09, 6.538479728756012e-13, 8832.440523256946, -37.52197446358211], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "XNN",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p0  c+1  {1,D}, {3,D}
3 N  u0  p2  c-1  {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.863304528558866, 0.0044727378996352735, -7.657888254030589e-06, 7.566551322548495e-09, -2.8240309396521113e-12, -4964.969731518212, -7.401146569539408], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411396737184059, -0.0016031840634147642, 2.8880078620045804e-06, -1.556323952810155e-09, 2.807779740962135e-13, -5330.642627873445, -15.027258594306273], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 56.8 and 56.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
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
            NASAPolynomial(coeffs=[-2.5739263830230383, 0.047739907569548025, -4.598070554827103e-05, 2.351354975713881e-08, -4.7455095408821535e-12, -8276.816764564823, 9.441519150074074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.908024758271736, -0.015549251038012276, 2.7772942266178536e-05, -1.484153246052161e-08, 2.6631323285942338e-12, -13591.695693042806, -94.6975853312059], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
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
            NASAPolynomial(coeffs=[-0.2993505590209032, 0.036295047104036034, -3.944358953629666e-05, 2.3073395624284446e-08, -5.505172706588013e-12, -16348.592670076328, -0.5243066765065851], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089051869291591, -0.009905142176605984, 1.769612743136704e-05, -9.4569990848886e-09, 1.6972918872508545e-12, -19991.367022096892, -73.24268995539349], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "XNHXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {5,S}
2 X  u0  p0  c0  {6,D}
3 X  u0  p0  c0  {7,S}
4 H  u0  p0  c0  {5,S}
5 N  u0  p1  c0  {1,S} {4,S} {6,S}
6 C  u0  p0  c0  {2,D} {5,S} {7,S}
7 N  u0  p1  c0  {3,S} {6,S} {8,S}
8 H  u0  p0  c0  {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4658840835034903, 0.04032671174813905, -5.1677635604570834e-05, 3.3783985926401025e-08, -8.785375205100365e-12, 5520.033302126237, 4.137115672641978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.158172157336903, -0.006887697575459862, 1.2286455919780816e-05, -6.5489391464297215e-09, 1.1738114261372569e-12, 2273.211823594911, -63.78765548494883], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
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
            NASAPolynomial(coeffs=[-2.335993439055977, 0.04095493966544115, -3.308964605037999e-05, 1.2340872982475107e-08, -1.0794767857369436e-12, -4138.3362195106965, 14.860345426691612], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.74976165361396, -0.015545093613927969, 2.7694717132704748e-05, -1.4747871407183279e-08, 2.63918260753589e-12, -9207.074848097625, -82.7716117653313], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 74.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
    label = "XOXCNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 X  u0  p0  c0  {4,S}
3 O  u0  p2  c0  {1,S} {4,S}
4 C  u0  p0  c0  {2,S} {3,S} {5,D}
5 N  u0  p1  c0  {4,D} {6,S}
6 H  u0  p0  c0  {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.138216103041777, 0.02823086411784676, -3.8437541152423604e-05, 2.6868203923619623e-08, -7.519328909522116e-12, -21406.67005006852, -5.622350233610955], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261952078333145, -0.004316973382806578, 7.73409680281726e-06, -4.144915494278597e-09, 7.462540784972105e-13, -23546.870003242817, -50.91355633230831], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "OXCNH2",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 O  u0  p2  c0  {3,D}
3 C  u0  p0  c0  {1,S} {2,D} {4,S}
4 N  u0  p1  c0  {3,S} {5,S} {6,S}
5 H  u0  p0  c0  {4,S}
6 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3347812981984684, 0.024001926445212443, -2.56561658286328e-05, 1.4867686876108568e-08, -3.5296973677212407e-12, -37457.85622667209, -0.6581843781404473], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997098052356328, -0.006795965625441362, 1.2045699322112889e-05, -6.359634936884278e-09, 1.1313346110218602e-12, -39913.89127158535, -49.545628505612484], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 37.01 and 60.96,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3768902555000424, 0.01716828893718684, 1.0226321143136432e-05, -2.3112247575109005e-08, 9.75945366188391e-12, -54273.124036769594, -7.590723086367682], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.381509301194935, -0.01483893474211383, 2.65610658179714e-05, -1.4250112374202607e-08, 2.5651784197483225e-12, -58495.72488622528, -81.64682914395209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 62.9 and 75.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
    label = "CH3XNXNOH",
    molecule = 
"""
1 X  u0  p0  c0  {7,S}
2 X  u0  p0  c0  {8,S}
3 C  u0  p0  c0  {7,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p1  c0  {1,S} {3,S} {8,S}
8 N  u0  p1  c0  {2,S} {7,S} {9,S}
9 O  u0  p2  c0  {8,S} {10,S}
10 H  u0  p0  c0  {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4985974573272718, 0.032355190208176496, -2.1571861406286484e-05, 4.167224639668699e-09, 1.1892153928272364e-12, -9225.046921788462, -0.5266906827411653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.60251185517201, -0.013353248368212221, 2.379894519605285e-05, -1.2680910283828348e-08, 2.2710678925289256e-12, -13602.681001284698, -83.39997325193697], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 43.28 and 91.29,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "XONH2",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 O  u0  p2  c0  {1,S} {3,S}
3 N  u0  p1  c0  {2,S} {4,S} {5,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3860267526578358, 0.016641787893430366, -1.6919429844757538e-05, 9.530135630943216e-09, -2.1792567750367198e-12, -8696.09227342195, -0.7177355154818166], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.443721041372171, -0.005684040584492491, 1.0035186919117291e-05, -5.2677860777462666e-09, 9.321823589864562e-13, -10498.551977432064, -36.467259613747544], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 32.89 and 61.93,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "OXNNH",
    molecule = 
"""
1 X  u0  p0 c0  {3,S}
2 O  u0  p3 c-1  {3,S}
3 N  u0  p0 c+1  {1,S} {2,S} {4,D}  
4 N  u0  p1 c0  {3,D} {5,S}
5 H  u0  p0 c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.932904977014775, 0.025594396730344988, -2.9929209749898772e-05, 1.7922495652637445e-08, -4.312904200443057e-12, -2158.558066675662, -4.323578107980424], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189909236154165, -0.004837276323957634, 8.704543634748917e-06, -4.700785411742493e-09, 8.512922744524252e-13, -4454.662622430416, -50.9038572152291], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "XNCO",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 N  u0  p1  c0  {1,S} {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.9093427832856398, 0.015109857567877763, -2.0359918968130758e-05, 1.4975405540619096e-08, -4.539493780875148e-12, -21677.28235937503, -3.1891958041489765], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.079628606140264, -0.002883577778149964, 5.257881761191409e-06, -2.8882247892031097e-09, 5.294853427979958e-13, -22938.005661268922, -29.032431347097084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 79.59 and 79.64,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "XCCH2",
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
            NASAPolynomial(coeffs=[0.3537232216404795, 0.02738047612849207, -3.8612604745333626e-05, 2.9270129615313785e-08, -8.860745470684606e-12, 12563.1134335633, -2.856833924551207], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50738886564937, -0.005965218577499618, 1.0615016854246257e-05, -5.630345050552874e-09, 1.0041366575849666e-12, 10425.230183503043, -48.18896116956779], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2710300707133886, 0.04275388669801405, -5.6165217605294374e-05, 3.8441904983893874e-08, -1.0600409439120995e-11, 12982.519070572595, 6.930604839386239], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.12906137260305, -0.007572217776039778, 1.360161547534432e-05, -7.320902085911084e-09, 1.3215775807826633e-12, 9546.17320087401, -64.82524264398151], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
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
            NASAPolynomial(coeffs=[-0.5280803860139417, 0.0285783252077775, -2.2234906966676733e-05, 7.78827990007637e-09, -5.933586955109149e-13, -26143.789971103004, 7.519427148206355], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978155171283714, -0.010727812123524144, 1.9236820173513977e-05, -1.0341454007115124e-08, 1.8645498454938642e-12, -29780.014140883155, -61.77930156020717], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 58.8 and 75.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "XNO",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8619810025490673, 0.012267703380084078, -1.7731758155958465e-05, 1.315536840698411e-08, -3.9401086560086895e-12, -13204.301021899753, -9.289693099202832], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.60325861290425, -0.0013940190087381843, 2.573613909741894e-06, -1.436315753114337e-09, 2.6664821685648044e-13, -14076.60512762568, -27.812281404482913], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
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
            NASAPolynomial(coeffs=[2.359495731431357, 0.026577899561492875, 4.854377666264913e-06, -2.3300751281310787e-08, 1.080241104900459e-11, -56331.89966840517, -2.7290965641338794], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.248882464739534, -0.01932093653813231, 3.441582389182342e-05, -1.8332031567445875e-08, 3.2816944758981732e-12, -61863.720374265205, -101.87030526237768], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.26079540729489786, 0.029660018341478807, -3.746238665500517e-05, 2.358568716943405e-08, -5.979147732482204e-12, -67629.99522160624, 4.317532672755526], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046796775039754, -0.003516390240860414, 6.491780792346332e-06, -3.6335189500432592e-09, 6.76298154237971e-13, -70005.46909477336, -44.67323784193456], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 89.5 and 92.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 122,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3891902594461783, 0.029211254914251555, -3.686302879714153e-05, 2.577719019942489e-08, -7.388346878745011e-12, -22840.000468295813, 3.258447821188735], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.099162358552885, -0.007408051053110082, 1.3248023640579377e-05, -7.084641349487045e-09, 1.2717661007009525e-12, -25460.568438289876, -50.37072313089001], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "XOH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.6898546774949579, 0.011560714377428666, -1.8172061719401493e-05, 1.4019483176817962e-08, -4.13411839483846e-12, -20428.633188374264, 2.129066713741218], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.9594002477034005, -0.0016598690893849198, 2.83126774534202e-06, -1.4039375937825617e-09, 2.3701080762369444e-13, -21107.367494599384, -13.688877268045676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 80.8 and 80.8,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 124,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.11893718001907885, 0.02541808705430347, -9.608108765723387e-06, -4.295199952049952e-09, 3.4643572732750982e-12, -10688.181078499601, -0.7380722583744292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060757899352813, -0.014857615759044823, 2.6463057211542945e-05, -1.408810404432668e-08, 2.519977482300052e-12, -14878.770402317108, -78.21199707340558], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 125,
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
            NASAPolynomial(coeffs=[-0.4556863016454771, 0.02637115066174354, -2.1193123690587854e-05, 8.24653183318703e-09, -8.510588067611735e-13, -10507.594973970969, 6.940746767287202], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091019819661316, -0.011033048767363404, 1.9484405869727385e-05, -1.0237438115629293e-08, 1.8128748895400622e-12, -13823.172152885534, -57.16805413486118], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 76.79,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 126,
    label = "XOXNO",
    molecule = 
"""
1 X  u0  p0 c0  {3,S}
2 X  u0  p0 c0  {4,D}
3 O  u0  p2 c0  {1,S} {4,S}
4 N  u0  p0 c+1  {3,S} {2,D} {5,S}
5 O  u0  p3 c-1  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9935294751058956, 0.019188084816283715, -2.42924974394525e-05, 1.547804984753989e-08, -3.9995055878261354e-12, -22647.38076822519, 1.4913827637688648], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.354995216279332, -0.002362726178059236, 4.3611695875785825e-06, -2.4396473219602613e-09, 4.538698078124497e-13, -24195.914141323527, -30.368866436801472], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 63.4 and 94.07,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7686539476068672, 0.015420898484374354, 5.767884406987405e-06, -1.5827045233451258e-08, 6.751805711746606e-12, -30120.301602978834, -5.059392156151771], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.847749730759535, -0.01335819566033185, 2.386893017993304e-05, -1.2769340121425279e-08, 2.2930531883285244e-12, -33716.20801141649, -68.67480546580957], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 30.5 and 72.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
    label = "XNXNO",
    molecule = 
"""
1 X  u0  p0  c0  {3,D}
2 X  u0  p0  c0  {4,D}
3 N  u0  p1  c0  {1,D} {4,S} 
4 N  u0  p0  c+1  {2,D} {3,S} {5,S}
5 O  u0  p3  c-1  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.331038987128432, 0.024146747684085316, -3.506375863681946e-05, 2.529019734254638e-08, -7.2690325980673265e-12, 4631.466671581334, -6.608669248279261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420686007412883, -0.002119684347932115, 3.923924112852273e-06, -2.199553140841385e-09, 4.098201473816919e-13, 3015.808489172159, -41.566088246820584], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4414185422025114, 0.020141843913278987, 1.004446940309389e-05, -2.4632473249166706e-08, 1.0643652625930144e-11, -32702.781832929493, -2.162546111921909], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.599268479100633, -0.01794421988237652, 3.1880937783277695e-05, -1.6915783501947735e-08, 3.0187083572847523e-12, -37500.606248470125, -87.2751835535458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
    label = "XNCNH",
    molecule = 
"""
1 X  u0  p0  c0  {2,S}
2 N  u0  p1  c0  {1,S} {3,D}
3 C  u0  p0  c0  {2,D} {4,D}
4 N  u0  p1  c0  {3,D} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.8242951099574672, 0.02601749300527663, -3.764243998419181e-05, 2.8538878383309112e-08, -8.616187624488347e-12, 8533.633778049416, 0.7718232648179626], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101373002612124, -0.004568081627199246, 8.155009679545203e-06, -4.344213509050772e-09, 7.779513439557439e-13, 6625.471826454845, -40.10485955343061], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 54.13 and 75.02,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
    label = "XNNCH3",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.230754474365933, 0.017783658337877685, -5.881534702396693e-06, -3.712415964603129e-09, 2.534902843187581e-12, 5003.312491684974, -3.1752208193723153], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925748183648, -0.010525828837205065, 1.8814014384299243e-05, -1.006660382450365e-08, 1.8080350821928545e-12, 1965.1331915530463, -58.79212788139595], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 60.41 and 70.27,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 132,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.638128311790396, 0.011236540999882609, 3.664844911067219e-06, -1.1120657164061452e-08, 4.8571719563073046e-12, -20003.403531453092, -2.018462765805568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.252954055242327, -0.009480301245285542, 1.6901229048930064e-05, -9.011985872256507e-09, 1.6141330283557347e-12, -22550.496235636147, -47.321051295023864], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 133,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.09380422645656587, 0.03254184716882104, -1.9508073897544622e-05, 1.9033590070599593e-09, 2.0178511639379337e-12, -35548.33244324537, 5.477417787388822], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.823623671029893, -0.015032614497108913, 2.673269143470952e-05, -1.419836836264027e-08, 2.535846969827513e-12, -40170.28527060442, -81.69221157337572], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 96.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 134,
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
            NASAPolynomial(coeffs=[-3.0932804254633512, 0.04054757010622049, -5.061867190583267e-05, 3.338407760784367e-08, -8.850732646781267e-12, -2549.7885794155977, 11.04447440181341], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340397884578818, -0.0088565986454187, 1.5767249042201063e-05, -8.379519466619423e-09, 1.497433921245116e-12, -6038.756874638924, -61.114477479073585], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 135,
    label = "CH3XNNOH",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p0  c+1  {1,D} {3,S} {7,S}
3 C  u0  p0  c0  {2,S} {4,S} {5,S} {6,S}
4 H  u0  p0  c0  {3,S}
5 H  u0  p0  c0  {3,S}
6 H  u0  p0  c0  {3,S}
7 N  u0  p2  c-1  {2,S} {8,S}
8 O  u0  p2  c0  {7,S} {9,S}
9 H  u0  p0  c0  {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.8458767372850369, 0.029847037326815637, -1.6288060107211608e-05, -5.160668468083551e-10, 2.7107066591369744e-12, -9958.975006687913, -2.262003683764842], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.56413769242538, -0.01346431811154401, 2.3999175935712788e-05, -1.2790808184361166e-08, 2.2913064369846966e-12, -14298.071544804574, -83.4757358547679], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 26.19 and 53.11,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 136,
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
            NASAPolynomial(coeffs=[0.8122506955542943, 0.02240816943062234, -2.560540942880489e-05, 1.573713386046396e-08, -3.913543100697581e-12, 9327.284163558212, -4.914017566653307], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420923212444105, -0.005908523822900844, 1.0467898149707035e-05, -5.523251266533882e-09, 9.815551844217065e-13, 7188.599038651622, -48.23756065490732], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 137,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3179838467359952, 0.03378081534288041, -1.4799606364101423e-05, -3.849161364955791e-09, 3.936379000535339e-12, -37220.07459732981, 3.571976723406868], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33780951406004, -0.017434394968453903, 3.119767889977107e-05, -1.6722666366243355e-08, 3.0079833819606806e-12, -42560.66815624071, -95.0724895175665], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 63.5,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 138,
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
            NASAPolynomial(coeffs=[-4.872530990892688, 0.05562110739421251, -6.411740846381472e-05, 3.90946383572137e-08, -9.649864241012551e-12, 5914.924768678297, 18.42848547630861], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033258703301918, -0.013087062152820088, 2.3459289825218143e-05, -1.259972074761509e-08, 2.27017642762139e-12, 710.5687274694483, -86.81233037475391], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 139,
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
            NASAPolynomial(coeffs=[1.8969967399970498, 0.03136537278382585, -3.453660942774956e-05, 1.938036117537774e-08, -4.250745588851856e-12, -81227.7703015737, -0.6822241363351544], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.83415680377455, -0.007126677188177576, 1.2639040075343967e-05, -6.681795799640911e-09, 1.1906517912991903e-12, -84216.8621126562, -60.909943049190474], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 37.3,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 140,
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
            NASAPolynomial(coeffs=[0.25283229666286844, 0.02196083615973443, -2.9950780653634024e-05, 2.1358393509157084e-08, -6.125745743990052e-12, 7647.689375827132, -2.7225950490932895], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479256089403834, -0.003801893741304097, 6.806689659541158e-06, -3.6435473720240567e-09, 6.55030932313473e-13, 5944.470314248284, -38.61818128245971], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 141,
    label = "OXCXCH2",
    molecule = 
"""
1 X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.6497117249237597, 0.03554659990718607, -4.4142697799558037e-05, 2.93903593051855e-08, -8.001765916532122e-12, -31065.329535987556, 1.807676305525411], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.113681847679658, -0.007676997669985588, 1.3787877482188212e-05, -7.421194660802826e-09, 1.3394167722781966e-12, -34192.46412685221, -62.165190770593796], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 142,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.41436465043911636, 0.029786625133376217, -2.426107781057743e-05, 8.221441058744636e-09, -2.817850119907206e-13, -29333.09019851374, 7.219061486102157], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.025013580421547, -0.009793659831366196, 1.7460964722192518e-05, -9.310410292910685e-09, 1.6689305407764036e-12, -32896.85373056611, -61.54133917364577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 51.0,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 143,
    label = "XNHOH",
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
            NASAPolynomial(coeffs=[-0.010038189100148368, 0.027915951531930515, -3.7008074488711533e-05, 2.570289914908294e-08, -7.117882672158515e-12, -11488.059945739693, -1.4839360217744142], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.46433498705958, -0.005614607763985756, 9.924580262988197e-06, -5.215372068440793e-09, 9.23919913422026e-13, -13720.164437243038, -48.57071566492603], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 144,
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
            NASAPolynomial(coeffs=[-3.4051441867506744, 0.047724289490958145, -6.43559924429585e-05, 4.449797963339486e-08, -1.2296011431267573e-11, 10665.650093134778, 11.83631806740635], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.134869945412417, -0.0075269187342327185, 1.3520541327636236e-05, -7.277197774712797e-09, 1.3138262992731103e-12, 7014.222289287651, -65.34142221287271], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 145,
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
            NASAPolynomial(coeffs=[-1.3776098886368788, 0.03725658652985835, -5.301683192936591e-05, 3.855549170243632e-08, -1.1193462823300138e-11, -26977.184943178, 3.9622718582434455], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.198849403954185, -0.005117172932029725, 9.263940504945724e-06, -5.038401040839732e-09, 9.169576549613017e-13, -29650.63289276218, -53.26801022581537], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 146,
    label = "NNOX",
    molecule = 
"""
1 X  u0  p0  c0
2 N  u0  p2  c-1  {3,D}
3 N  u0  p0  c+1  {2,D} {4,D}
4 O  u0  p2  c0  {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.923562143240646, 0.010682159200923623, -1.2508195264134207e-05, 8.481349940250621e-09, -2.4795755726447766e-12, -4009.732963747003, -2.176705532413184], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.086216049969408, -0.0028051611886139994, 5.098960366822314e-06, -2.7909116737181186e-09, 5.101968931763034e-13, -5077.667642364492, -23.237580035600725], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 147,
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
            NASAPolynomial(coeffs=[-4.002408677490918, 0.05221889029432998, -5.891216152170422e-05, 3.5103548702661736e-08, -8.419341612775355e-12, -2610.5415056517586, 15.082182270412012], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.9486679253505, -0.012883729841375003, 2.302832738699371e-05, -1.2316759623532165e-08, 2.2120213375841774e-12, -7594.999852063423, -85.45366806841204], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 148,
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
            NASAPolynomial(coeffs=[-3.2454263842040563, 0.045740712834499, -5.206788394779641e-05, 3.1011581474928596e-08, -7.431173731919927e-12, 4236.247633353321, 14.227506587622653], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973737140881015, -0.010520315933265804, 1.8851700221785156e-05, -1.0120427938433633e-08, 1.8231167545404697e-12, -60.118641661396396, -72.51992728662742], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 149,
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
            NASAPolynomial(coeffs=[-0.300412672194553, 0.036196155908658725, -4.2884290614632455e-05, 2.714169514084154e-08, -6.9348485287612505e-12, -22771.85297608239, 5.483638123808867], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191116478633521, -0.00886431129373155, 1.5729147271793533e-05, -8.318780340166752e-09, 1.4811271173832512e-12, -26089.03741350082, -62.242630748054566], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 150,
    label = "XCOOH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3590540257949546, 0.02501724558325153, -3.0958732097422e-05, 2.0028686967558853e-08, -5.265201469262237e-12, -57731.94726602654, 3.52733979234295], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.1626551705247, -0.004701472115306819, 8.43556603182292e-06, -4.533668267548416e-09, 8.179721904287085e-13, -59883.66819438679, -40.59755552516822], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 36.7 and 64.6,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 151,
    label = "XOXNH",
    molecule = 
"""
1 X  u0  p0  c0  {3,S}
2 X  u0  p0  c0  {4,S}
3 O  u0  p2  c0  {1,S} {4,S}
4 N  u0  p1  c0  {2,S} {3,S} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.26696039959774404, 0.025658708019581325, -3.6746089354556215e-05, 2.652568290254523e-08, -7.56687767999864e-12, -6665.082742258265, -0.5999011793376585], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589736849916923, -0.0034428159868778517, 6.1541249150112485e-06, -3.2864385949829006e-09, 5.898563049065437e-13, -8449.405834331501, -39.32243587207851], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 152,
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
            NASAPolynomial(coeffs=[-3.484480061504159, 0.049611889732151956, -4.654198224495474e-05, 2.2377925953709398e-08, -4.031094902323673e-12, 1043.6369007785365, 13.750530599079733], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886825386143485, -0.015838525349654065, 2.8325178735322635e-05, -1.5167316715817698e-08, 2.7260964210844285e-12, -4523.308930025074, -95.0345997749903], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 153,
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
            NASAPolynomial(coeffs=[-4.026345852130678, 0.050330824582074225, -5.385881175406401e-05, 3.034074169321413e-08, -6.849180944623612e-12, -1839.3279882527127, 15.773763750300732], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.89638211689794, -0.01326625399305861, 2.3747362731478014e-05, -1.2730778062976612e-08, 2.2905149321293325e-12, -6892.300734531827, -84.98132493424458], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 154,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.40376886767600445, 0.03434773773851405, -1.589336246930892e-05, -2.4397393198112853e-09, 3.409550419775087e-12, -10123.123570761636, -2.8137786594112715], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.778567406809294, -0.018507705596035758, 3.304254534572872e-05, -1.7651525659642544e-08, 3.1660737399852312e-12, -15530.527793383451, -103.13119150373578], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 155,
    label = "H2OX",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7297147696519386, 0.008710513433113376, -1.2913175453546773e-05, 1.0729495025872316e-08, -3.3943334254438184e-12, -32612.699921535637, -6.044799612763292], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854969755224983, -0.0032884838154521837, 5.569914961149535e-06, -2.7300853163986106e-09, 4.558987651233143e-13, -33304.637773603696, -21.351875463188136], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 62.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 156,
    label = "XNCN",
    molecule = 
"""
1 X  u0  p0  c0  {2,D}
2 N  u0  p1  c0  {1,D} {3,S}
3 C  u0  p0  c0  {2,S} {4,T}
4 N  u0  p1  c0  {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.3087966439268551, 0.023227065095417408, -3.556983029780869e-05, 2.775356125764918e-08, -8.585455263387942e-12, 13996.791175076749, 2.811366711504294], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.115613052476612, -0.0028051889306885385, 5.132717569782909e-06, -2.8290128457275187e-09, 5.200085899533489e-13, 12463.136578892016, -30.609649770950455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 88.08 and 88.09,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 157,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4742019619819957, 0.042144995536667125, -5.019755499211274e-05, 3.192281341306676e-08, -8.249907701429748e-12, 8412.679148354388, 6.3646605945007675], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.113333075018854, -0.009852181996058411, 1.760958052368724e-05, -9.414965035147297e-09, 1.690377726709007e-12, 4567.741898875414, -71.922418943132], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 158,
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
            NASAPolynomial(coeffs=[-0.5193148349166338, 0.023734401542306514, -2.1291541552457206e-05, 9.945549656770349e-09, -1.7005320762653042e-12, -8276.829956220929, 7.353465918619756], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145639013678018, -0.008751777752192158, 1.5480383746770106e-05, -8.152097424369403e-09, 1.4464151515511565e-12, -11060.98026592037, -46.971396464133335], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 24.5 and 55.12,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 159,
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
            NASAPolynomial(coeffs=[1.0741274556154028, 0.022965576621378495, -1.2260547570099876e-05, -1.2460321254102096e-09, 2.540360283243004e-12, -44791.61028426065, 1.029548333678978], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048629858122181, -0.009848436466281987, 1.7567229443068718e-05, -9.375556766452995e-09, 1.6816185962709e-12, -48097.56898300494, -60.86273230058802], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 42 and 64.2,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 160,
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
            NASAPolynomial(coeffs=[-4.808912278042515, 0.05371459353605084, -6.677816098958233e-05, 4.3278250548889796e-08, -1.1302327129758538e-11, 7472.312759577584, 17.84935288787215], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.066244577410863, -0.010480168414818717, 1.881927352100178e-05, -1.0130741835721841e-08, 1.8288358396851678e-12, 2888.074211628449, -76.61936010724799], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 161,
    label = "NCOHX",
    molecule = 
"""
1 X  u0  p0  c0
2 N  u0  p1  c0  {3,T}
3 C  u0  p0  c0  {2,T} {4,S}
4 O  u0  p2  c0  {3,S} {5,S}
5 H  u0  p0  c0  {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.388779213631883, 0.014850706410940143, -1.8053000059341232e-05, 1.2700296345620905e-08, -3.7160309551698134e-12, -15036.34282584674, -8.571580661198478], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.154633162229366, -0.004498769503700408, 8.014673958761491e-06, -4.261303331914661e-09, 7.615166703060956e-13, -16471.793095536144, -37.550570154064005], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 46.11 and 61.53,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 162,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.3738267893184363, 0.02339769200062538, -1.9573560022432125e-05, 7.627197853066382e-09, -7.421147030228781e-13, -29384.26680145155, 6.579102040857689], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314149933698543, -0.008568719429804302, 1.5185530659546744e-05, -8.022793154085987e-09, 1.4272203295633218e-12, -32196.77062464246, -47.98962958885656], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 25.3 and 72.1,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 163,
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
            NASAPolynomial(coeffs=[-4.541835805809122, 0.05160727391403616, -6.99488944443476e-05, 4.8515824081931226e-08, -1.345649286443873e-11, 14281.99245197646, 16.518000967056917], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143041715945822, -0.007834179492609282, 1.4122672211551237e-05, -7.640534691801569e-09, 1.3848751382857308e-12, 10364.802174466271, -66.32293547709035], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 164,
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
            NASAPolynomial(coeffs=[0.6073983748266721, 0.024113459272879424, -3.6226375705033655e-05, 2.7097576274857764e-08, -7.934382317831279e-12, -10251.979895977309, -4.173499030987074], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644644146453326, -0.0029201102305442955, 5.16968190751061e-06, -2.718904777923171e-09, 4.8236485420246e-13, -11800.355957951706, -38.614889737699016], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 165,
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
            NASAPolynomial(coeffs=[-1.0343560218929917, 0.02954889213174962, -3.7388956403900184e-05, 2.5054277182663535e-08, -6.773304139784386e-12, -3550.2726794719283, 2.7569531883392795], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.38499187571051, -0.0062701685659363425, 1.1163513168188612e-05, -5.931883768833952e-09, 1.0601000397067635e-12, -6064.387350285909, -49.30415707094812], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 166,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.4078333893607506, 0.03381796177566529, -1.8236476569497745e-05, -2.1781846529770775e-10, 2.782378494270432e-12, -15300.852663274578, 3.0339536257089286], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695307434024926, -0.01618740727690008, 2.8912158147894964e-05, -1.5456094995757705e-08, 2.774248536517414e-12, -20306.325408676203, -90.50560326972989], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 167,
    label = "XN",
    molecule = 
"""
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0434374026493032, 0.017236903600525225, -3.068695772385649e-05, 2.538824345082357e-08, -8.015095531721528e-12, 5330.741161908639, 3.0546208304970115], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8710250803063295, -0.000459583897810385, 8.695024882748882e-07, -4.943281589731255e-10, 9.304088132376496e-14, 4594.717977250466, -15.466780891576455], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 168,
    label = "XCH3",
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
            NASAPolynomial(coeffs=[-0.044452913308908576, 0.019436759636543545, -1.9102857378165163e-05, 1.1126926094899282e-08, -2.737358950621882e-12, -6388.038023546711, -0.1733858789314926], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657045298440448, -0.007903077857146142, 1.4010043902444632e-05, -7.4001607786229035e-09, 1.3151659242308404e-12, -8635.984505244489, -44.33525482701773], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 169,
    label = "ONNH2X",
    molecule = 
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 N  u0 p1 c0 {3,S} {5,S} {6,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}


""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.763419916108498, 0.021946448969719, -2.103316059025525e-05, 1.0462346509861043e-08, -2.00841426822862e-12, -9469.628716040226, -2.2565505771061716], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.110541682510993, -0.006805474008018404, 1.2093550174710639e-05, -6.412294549468917e-09, 1.1443172374703573e-12, -11894.911951536622, -49.79891523032214], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 18.68 and 56.21,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 170,
    label = "XH",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.075699468841116, 0.017358077343272296, -2.609206412898108e-05, 1.8928216959216332e-08, -5.388359897162687e-12, -3166.189954018708, 8.153606339477767], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.7224745129276777, -0.0010681624758273717, 1.9865280608509053e-06, -1.120480196821236e-09, 2.0981090637377155e-13, -4218.234627879561, -15.320705237248276], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 171,
    label = "XNHNO",
    molecule = 
"""
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {5,S}
3 N  u0 p1 c0 {2,S} {4,D}
4 O  u0 p2 c0 {3,D}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.9423372093417675, 0.02493487343959535, -2.7919420506031866e-05, 1.5719571712970995e-08, -3.4902289391958163e-12, -8459.511244295209, -4.565914187237134], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170222985061477, -0.004832591811848306, 8.689196070678313e-06, -4.688316791083182e-09, 8.486224638721293e-13, -10772.33474112986, -51.128817254636154], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 172,
    label = "XCCO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 X u0 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.48229906536793415, 0.02587155127531559, -3.9360365788694726e-05, 3.0462959888373194e-08, -9.365327957588931e-12, -20116.830703860825, -3.573773358707397], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.0708325244702, -0.0030085351441184282, 5.5154130366392516e-06, -3.0480644218682132e-09, 5.614704876502467e-13, -21831.51750651156, -40.86266658834928], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 173,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.0278046479993272, 0.04868277469861659, -4.646973264049378e-05, 2.2875158469816263e-08, -4.2387759968676164e-12, -9837.038578469623, 11.50704836401261], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.77877011492434, -0.015532217068462958, 2.7689854090790898e-05, -1.4757543334478308e-08, 2.6427560802981618e-12, -15224.110665974582, -94.26062897519923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 174,
    label = "XNH",
    molecule = 
"""
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.7556935991113143, 0.02931258322046972, -4.843786135235457e-05, 3.8446894497971926e-08, -1.1723805953822719e-11, -978.8809973477827, 10.096496473865535], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.828393274330211, -0.0024595949286131567, 4.346762608100847e-06, -2.2753101158881143e-09, 4.018659752232502e-13, -2516.3366820771976, -26.3700032711956], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 175,
    label = "NNX",
    molecule = 
"""
1 X  u0 p0 c0 
2 N  u0 p1 c0 {3,T}
3 N  u0 p1 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.177331860342677, -0.0012986530515051672, 2.5984608392459963e-06, -9.710009093628354e-10, -9.263358309585801e-14, -5055.013851680827, -7.8361280056985745], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824912386021, -0.0015051356127564913, 2.6825671580396526e-06, -1.4261829223683117e-09, 2.5443162032394223e-13, -5165.918600128985, -9.19892716405165], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 9.93,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 176,
    label = "XNXCXNH",
    molecule = 
"""
1 X  u0  p0  c0  {4,D}
2 X  u0  p0  c0  {5,D}
3 X  u0  p0  c0  {6,S}
4 N  u0  p1  c0  {1,D} {5,S}
5 C  u0  p0  c0  {2,D} {4,S} {6,S}
6 N  u0  p1  c0  {3,S} {5,S} {7,S}
7 H  u0  p0  c0  {6,S} 
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.685978627729595, 0.025296468804795018, -3.4398724583518516e-05, 2.4726462848270053e-08, -7.1681376112575634e-12, 8515.098366500077, -8.130952558650874], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122123532985963, -0.004680413880020813, 8.377743678764652e-06, -4.483216274102132e-09, 8.058110283909199e-13, 6516.202102220586, -50.07405596097429], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 177,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.1209839650654505, 0.03948489337397223, -5.467134560713659e-05, 3.872997294685073e-08, -1.0891107460331284e-11, 451.9436576678357, 11.198399654770991], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50733559911769, -0.0062944615865850465, 1.1259999982182603e-05, -6.0234545814607654e-09, 1.0820098750351573e-12, -2470.080207671811, -51.2967294712286], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 178,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.14003259781996247, 0.03586162976285301, -1.11021364991019e-05, -8.973999424710427e-09, 5.916364620439651e-12, -15015.360193922505, -0.9771971470803091], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.506545750084097, -0.021538701603008723, 3.84134172767583e-05, -2.049047834779493e-08, 3.67104278562163e-12, -21138.773353114368, -113.46375175738402], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 179,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.5930036410580237, 0.03571236960277976, -2.8891917695947535e-05, 1.0353989429743649e-08, -6.877484692857649e-13, 6188.130000196573, 4.071108868409096], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.859740958863316, -0.012892229650732454, 2.2989923173715027e-05, -1.2260637510722244e-08, 2.1968922551084385e-12, 1820.466660714781, -80.0996968777047], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 180,
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
            NASAPolynomial(coeffs=[-1.0485328055132175, 0.028672112331914735, -3.4822695375238e-05, 2.2596349194893594e-08, -5.960530680138021e-12, 2061.869447615992, 2.5065656904453557], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414361625368064, -0.006532492926442659, 1.1674964208927885e-05, -6.240271609019632e-09, 1.1201413670854261e-12, -504.9214239416051, -49.97073415880129], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 181,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.3828187309797452, 0.031836903255905415, -4.013910077551464e-05, 2.761968717216655e-08, -7.788499012395533e-12, 11491.801571653079, 5.759655127568052], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118039767476288, -0.0074059749629245735, 1.3261664190103652e-05, -7.105185250480473e-09, 1.2776281650071471e-12, 8680.11986425383, -51.83453946208235], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
The two lowest frequencies, 12 and 99.7,where replaced by the 2D gas model.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 182,
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
            NASAPolynomial(coeffs=[0.7048343312416007, 0.028376201417515148, -3.7864509437051594e-05, 2.6544109758791067e-08, -7.541790109089064e-12, 33604.98339794909, -4.371824159907967], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.196869682854762, -0.004925420385461617, 8.881818762142402e-06, -4.805481378877049e-09, 8.710592807486574e-13, 31336.47745454246, -51.66537239982247], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 183,
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
            NASAPolynomial(coeffs=[-1.236169616951722, 0.0391192964347373, -3.594452974308101e-05, 1.7078239755369327e-08, -3.0713001586413213e-12, -6077.114394037311, 3.5450552454458464], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.907361423361152, -0.013048576275606832, 2.3318786109779613e-05, -1.2471542891601062e-08, 2.239508305499705e-12, -10565.863727883938, -83.81982158180084], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 184,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0128277676926316, 0.039605453245976766, -2.4179579834566663e-05, 3.2356519006891704e-09, 1.993148701640024e-12, -10478.951788716044, 3.3418135904896475], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.5941142062787, -0.018498140954926762, 3.29579995577773e-05, -1.7553526856730535e-08, 3.1414002936479626e-12, -16112.312088730263, -102.82843075468661], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 185,
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
            NASAPolynomial(coeffs=[0.2631703605638592, 0.02672958182700725, -2.8237311149280387e-05, 1.6164539099028483e-08, -3.69835412294961e-12, 5409.001850176296, -2.446254248524509], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.199486664560553, -0.008342041650362158, 1.4711414998931697e-05, -7.709954680296734e-09, 1.3627206815362359e-12, 2648.6637193944116, -57.70149463482577], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 186,
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
            NASAPolynomial(coeffs=[-1.2597947854333764, 0.042911061194315925, -6.112561275165806e-05, 4.481050517474996e-08, -1.3045467484040785e-11, 19827.635343906535, 3.5252823923395966], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261909294145994, -0.006846950029475659, 1.2247928231585094e-05, -6.547805246035505e-09, 1.1756090977137418e-12, 16722.452170654033, -63.24393195054921], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 187,
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
            NASAPolynomial(coeffs=[1.600791364726406, 0.014704845247362895, -1.4669740619650143e-05, 6.819304873825679e-09, -1.1479810158032677e-12, -22934.494013238454, -0.766296623165708], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295792299031667, -0.0025855513420097, 4.764106999098455e-06, -2.6619189543733584e-09, 4.947908487145042e-13, -24420.494274960743, -29.782781634319207], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
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
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 188,
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
            NASAPolynomial(coeffs=[-0.6781890175202328, 0.03266563196550605, -3.482124141809595e-05, 1.9201333508215776e-08, -4.230282790729234e-12, -23656.67706119554, 1.4808105805832952], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110986738337399, -0.007888949731124329, 1.419017817690404e-05, -7.661299725244604e-09, 1.3863367885039082e-12, -26913.36744121951, -63.26475767863039], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
        ],
        Tmin = (298.0,'K'),
        Tmax = (2000.0,'K'),
    ),
longDesc = u"""
Calculated by Kirk Badger at Brown University using statistical mechanics methods implemented in
Franklin Goldsmith's thermo_kinetics_scripts repository in the new_workflow folder:

https://github.com/franklingoldsmith/thermo_kinetics_scripts/tree/main/new_workflow

DFT calculations were performed with Quantum Espresso using PAW pseudopotentals and the BEEF-vdW
functional for an optimized 3x3x4 supercell with the bottom 2 layers fixed. The following settings
were applied: kpoints=5x5x1, ecutwfc=50 Ry (60 Ry single point evaluation after),
smearing='marzari-vanderbilt', degauss=0.02, mixing_mode='local-TF', conv_thr=1e-12, fmax=1e-3.
""",
    metal = "Pt",
    facet = "111",
)

