
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
            NASAPolynomial(coeffs=[1.0132778475072701, 0.03262763570826161, -3.706098829519851e-05, 2.096041512034588e-08, -4.666933663368346e-12, -70967.1755533581, -4.753586717239662], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.852353741526818, -0.005708248771628979, 1.0285808664489898e-05, -5.5671600419076475e-09, 1.0106531250678213e-12, -73924.19842778567, -64.4494113654015], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.05960797334289609, 0.03493563179785079, -4.398561818752676e-05, 2.8727549381806642e-08, -7.522184645376874e-12, -26553.183793921464, -0.9051605772428148], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.07287735885974, -0.006643054324028648, 1.1791965140297656e-05, -6.237700413870547e-09, 1.111682612152697e-12, -29474.314843712473, -61.52688926912836], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.877926926018985, 0.028356310536416594, -4.27751405595965e-05, 3.274077611649272e-08, -9.758152617596373e-12, -2857.448955331013, 6.329231873570521], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.669218379280845, -0.004662997136616308, 8.163992478800666e-06, -4.22273875388183e-09, 7.383915821140929e-13, -4733.081559261902, -35.465579501976876], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.9656054071710813, 0.013397842441605466, -1.3429359698879124e-05, 7.121759804634978e-09, -1.4106305661109214e-12, -20699.095884215425, -6.1546523686721635], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.635376251400526, -0.004641483777463747, 8.092559149386185e-06, -4.167621187144764e-09, 7.263869522432795e-13, -22128.234824057938, -34.81280243590919], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.9262932796121506, 0.023921004692768495, -1.1102918161626347e-05, -3.2747211975357822e-09, 3.464924139989679e-12, -50572.40084185379, -0.7623442713754827], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.909721596928078, -0.011497684020644824, 2.0325676143003355e-05, -1.0702604898194835e-08, 1.899473932116419e-12, -54152.62193726688, -67.87697442298094], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.29622369517212804, 0.02186183598379325, -2.384164195327169e-05, 1.4095782512041287e-08, -3.388227788601993e-12, 2820.7450031023563, 6.207209502509924], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.412935045586693, -0.006234434296823646, 1.1089336157187554e-05, -5.8875825683398205e-09, 1.0512707211779502e-12, 624.0036006381906, -37.771499473057574], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.498039395513927, 0.02876142959338943, -2.6886230574547702e-05, 1.5278328810911775e-08, -3.7822969755660525e-12, 13453.989835671622, -1.115199210254696], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.832716581032793, -0.012370316735123905, 2.1968656798661015e-05, -1.1633963119097557e-08, 2.0721767242290296e-12, 9957.4015992165, -69.01643773841533], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.213713160033383, 0.012214685594674946, 1.9068661894472453e-05, -2.864543322553431e-08, 1.1057901204485512e-11, -17804.997259374402, -3.3273177063493993], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.869139569199708, -0.017678330250800806, 3.144153088580285e-05, -1.6706169144493843e-08, 2.983357568424075e-12, -22008.11270262748, -75.9101990058744], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.34654650041428675, 0.03320905703864805, -3.2298783640762634e-05, 1.775211080758764e-08, -4.033797332052941e-12, 12114.060943772498, 3.5866883402052956], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.940331279459487, -0.012270992404015326, 2.181434471467754e-05, -1.1572974866788502e-08, 2.064424650501198e-12, 8334.218456328797, -70.54964718014321], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.4289481587352657, 0.014037456723454458, -2.2117896236237133e-05, 1.7865958457623618e-08, -5.714789886892594e-12, -29337.782971544893, -7.782646256934949], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.486559647703558, -0.00168118059681464, 3.0902981422652133e-06, -1.7118642066550138e-09, 3.1586423018449393e-13, -30250.48241722518, -27.67881595007271], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.2935505382252128, 0.012551191160360839, -1.3054242917055773e-05, 7.661612183129024e-09, -1.921552545928318e-12, -1949.179227466059, -0.23896532416154947], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.516819543448202, -0.0038395525506032405, 6.878333551808847e-06, -3.6890043667521256e-09, 6.639622408293043e-13, -3300.717353376451, -26.758413738731676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3392481057648244, 0.015618794389118649, -1.7870610017897385e-05, 1.1610337082344122e-08, -3.208276115046275e-12, -23929.234602384662, -4.2782220447906925], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.472497740458118, -0.004256517883059183, 7.672396878603892e-06, -4.150940287875143e-09, 7.520569961562541e-13, -25490.911012841818, -35.277724916625566], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.3361010584116576, 0.022648346333239897, -2.3923922299082424e-05, 1.3725658402572206e-08, -3.2403205780927193e-12, -18407.675761841834, -1.8821437505641407], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.524883304404398, -0.00650732351743055, 1.1658610116104154e-05, -6.256799079108611e-09, 1.1264920930792274e-12, -20757.215384709063, -48.422483181893384], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.668054071556987, 0.02906936052545507, -4.8265363884475096e-05, 3.875892627442114e-08, -1.1974939840756911e-11, -2202.5553595330853, 9.729432728113348], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.904296267990244, -0.0026386471764010657, 4.717289404373525e-06, -2.5126685290206794e-09, 4.49659036145192e-13, -3748.807352288421, -26.710780698175974], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.339064957333164, 0.017984789974791308, -8.00999739794076e-06, -2.618487350352363e-09, 2.589055391050799e-12, 5067.0765912224015, 4.139062173736705], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.264096660326569, -0.009024670360010046, 1.603007829987153e-05, -8.50179159057831e-09, 1.516712565272404e-12, 2318.7111149044067, -47.2020183609326], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3072036645842438, 0.01659608503634022, -1.6559439093992738e-06, -8.536435228137193e-09, 4.498174256506795e-12, -1280.8588556629882, 1.009881570836706], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.18422183254375, -0.011502116906894708, 2.0395036676725923e-05, -1.0788035133151806e-08, 1.9199773506716312e-12, -4380.563556626077, -55.65810392016752], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.9091569530767527, 0.021534830198183502, -9.823273489797482e-06, -2.1902815248410317e-09, 2.4632884575771012e-12, 7224.572127586366, -8.927460895917271], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.863868938314901, -0.010727738459663648, 1.9186852775258245e-05, -1.0276919774530943e-08, 1.8476571148202874e-12, 3875.888213893726, -70.90072627641865], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.5500191363144759, 0.030684226099592187, -3.992253190972934e-05, 2.527832128135075e-08, -6.33311174031863e-12, -11139.490803174014, 4.895491072876913], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.242174539611717, -0.0029122593036831506, 5.3920077627840435e-06, -3.0311929831640128e-09, 5.661928516608506e-13, -13440.732414605254, -43.40465240510281], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.9451889695780322, 0.0395654328931119, -3.0393090947232115e-05, 9.792899750403322e-09, -1.9579980287692995e-13, -30405.63209384592, 13.106508558809036], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.78476659331341, -0.01522268158084659, 2.7096914983407928e-05, -1.4411830934704772e-08, 2.577083862658171e-12, -35408.259791801465, -82.85730670189777], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.2548024158707316, 0.037684796166005466, -3.935386042967999e-05, 2.167083364932704e-08, -4.778591670930258e-12, -752.67952920112, 4.101812082811877], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.93650714845121, -0.010360500448075585, 1.8520764227145175e-05, -9.908387788856631e-09, 1.7799921601873581e-12, -4629.793745435195, -72.84129128083454], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.45723412880679587, 0.02222624102464355, -1.667214371225305e-05, 5.7213606113744865e-09, -3.993230911289944e-13, -11043.637207150816, -2.2732381499886802], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.307104591573854, -0.009366253405579311, 1.671500714924329e-05, -8.92182977096838e-09, 1.5993403971733366e-12, -13965.245844046643, -57.941171527260124], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.9101484590607176, 0.03643406385183677, -4.2297594830785964e-05, 2.6415099718036338e-08, -6.6956047343197755e-12, -35254.17634198537, 8.346388315245013], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.917016607678658, -0.009266546203339028, 1.6416408390533058e-05, -8.660232696499291e-09, 1.5391694473332586e-12, -38680.492520939886, -61.19159179726639], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.370078260424586, 0.04528794010589457, -5.4441980887469694e-05, 3.4322575160957935e-08, -8.711860964962503e-12, -25028.719154091246, 8.336950553327528], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.054531012395937, -0.009769436336891313, 1.7438334882380193e-05, -9.305563906976561e-09, 1.6687295030874617e-12, -29053.828788761828, -74.0554468927241], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.6079274247270745, 0.03650728493459534, -1.730284393990231e-05, -2.6326843629503705e-09, 3.7728846009307856e-12, -9100.71629168968, 11.71799318595686], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.686830596872912, -0.018861777399497785, 3.369444181720986e-05, -1.8017040345429176e-08, 3.234259138790567e-12, -14756.22431056608, -93.34003419151713], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.153325540996552, 0.02312970459588002, -3.289593386747707e-05, 2.4411428167422815e-08, -7.243660680421592e-12, 7438.270186495325, -1.78965725929846], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.537086412571102, -0.0038577605328397446, 6.934780930064668e-06, -3.733044726040129e-09, 6.73801672644831e-13, 5723.962699519195, -38.320637292489366], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.7583066021087024, 0.042026433882833746, -5.6007583462955245e-05, 3.82518539347976e-08, -1.0409422587901935e-11, 6416.114706030231, 5.853459681963642], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.077462846206894, -0.0069399438622416995, 1.2365219150313984e-05, -6.576520786905656e-09, 1.1767578172919309e-12, 3162.4575252163177, -62.89442685237472], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.57898119013432, 0.03719159811617113, -1.2289813625810333e-05, -8.771769815563645e-09, 6.040393726449315e-12, -16729.95894363798, 1.472802312564843], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.536388899291097, -0.021593248247107222, 3.85299146386458e-05, -2.0569187126602726e-08, 3.6875590468852025e-12, -22972.894009237007, -113.39909883135287], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.2626202352689602, 0.023970714358677106, -3.5780723619742495e-05, 2.6941757996307356e-08, -8.087013323731892e-12, -11006.272709747118, -6.660739184973378], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.2901309587184, -0.0024479468693755285, 4.5124918164406676e-06, -2.513106859133e-09, 4.65786600128497e-13, -12602.368402143285, -41.25292166884209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.7981611203722376, 0.032699651187770046, -4.2566267050901004e-05, 2.9154268374034755e-08, -8.035869472649143e-12, -981.598852018363, 5.8480974735541835], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.43020619567617, -0.006459541211980741, 1.1544864226387672e-05, -6.169040761124964e-09, 1.107133468924275e-12, -3665.1870318123556, -50.122403724130024], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.3088630108107428, 0.028391709265768027, -3.0151763875375893e-05, 1.7719766305901612e-08, -4.275930323825351e-12, 2890.215065821995, 1.0285749140171498], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.348630310715528, -0.008905561261519528, 1.584617033231733e-05, -8.417565820461161e-09, 1.5032448006054834e-12, -72.78972125371183, -57.93258243300082], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.4723910057100326, 0.027761518099646696, -4.488254133969756e-05, 3.681377833423921e-08, -1.1613241694446062e-11, 21967.464262587568, 2.4118102932294203], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.532285266564477, -0.004937813113588516, 8.640818028709763e-06, -4.462037702098812e-09, 7.786519258654072e-13, 20256.691103903835, -36.665683365826], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8809039914295416, 0.018320066409276657, -5.853319874332877e-06, -4.761989758924705e-09, 3.300725492367627e-12, -826.6412044019955, 1.698875122279139], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.862710856228627, -0.01120309190514449, 1.9721635285657975e-05, -1.0314969449145613e-08, 1.820101472219746e-12, -3887.4842387359877, -55.20392925126269], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.5496448536768117, 0.018460052664930764, -2.420013043958681e-05, 1.734750800770796e-08, -5.04183408283732e-12, -19738.429102419694, -4.24774323354594], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.099133921015243, -0.004400167983064868, 7.814523835520559e-06, -4.134661955109478e-09, 7.364131855299469e-13, -21314.466233765193, -36.920955898799505], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.498423782159121, 0.0474505594410462, -6.331785137282016e-05, 4.414455225307518e-08, -1.2310077748727977e-11, -2411.5029453336074, 16.950244704069053], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.436432157703537, -0.009004093591465648, 1.6092779285333615e-05, -8.599467844927082e-09, 1.5431087837697012e-12, -6173.874870323905, -62.25645943135913], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[4.152111069111733, -0.0005487136273772019, 1.6858931205052016e-05, -1.8335787125524252e-08, 6.296303839543154e-12, -18010.214419124015, -11.442038340089166], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.405125044308313, -0.0069021689869445116, 1.2352154573210491e-05, -6.623629729186611e-09, 1.1913644594177635e-12, -19491.293310315763, -34.841792023764626], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.732877600588691, 0.032263436494000416, -3.779591319510644e-05, 2.3986557358586064e-08, -6.1615645684535194e-12, -968.2075242978414, 1.358875658034778], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.00012320321141, -0.008557071716915946, 1.5075778926318001e-05, -7.885502242007916e-09, 1.3920655190096632e-12, -3991.8075126146696, -60.25998041684972], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.3569778757199953, 0.016581801883417895, -8.932474616790587e-06, -5.965905632470024e-10, 1.6571137589950335e-12, -47308.023838223926, -0.5431885341088076], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.047788305582113, -0.007242739512152523, 1.290909747557425e-05, -6.880213112520502e-09, 1.2328951816120001e-12, -49711.33824829413, -45.47282931613026], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.0573753449463164, 0.01286243878960689, 4.849272541943912e-06, -1.3599710788744057e-08, 5.968999350557005e-12, -30311.486382253264, -12.43589373878602], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.113485231224725, -0.011408786351120009, 2.0203000713092304e-05, -1.0664783051023778e-08, 1.8954586961368203e-12, -33268.916892097055, -65.26660291889917], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.25761219966251164, 0.01938117613251084, -2.996922361248021e-05, 2.2777230292001347e-08, -6.8267985241454504e-12, 28603.240091191077, -2.704184347702303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.608147766904769, -0.0014237767361481668, 2.6419854059303414e-06, -1.4829002076982852e-09, 2.7654025856037765e-13, 27429.14282052521, -28.854150827357866], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.9682768211207824, 0.04821228035833279, -7.020388155243452e-05, 5.07019375283792e-08, -1.4459936798820567e-11, 20989.563730581798, 14.062551380934828], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.256195376093228, -0.005010585064278847, 9.09125751045964e-06, -4.959987133059913e-09, 9.052420251220165e-13, 17787.25662428015, -55.908645457779606], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.590355919069934, 0.028202952669437616, -4.319208631239718e-05, 3.320671683572305e-08, -1.0016173961611189e-11, 17113.544130645616, 0.22478511701380643], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.592987760441739, -0.003510015504528057, 6.290997253182512e-06, -3.3685267504343616e-09, 6.056105534205311e-13, 15311.777343123224, -39.79602226038769], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.44425495219864597, 0.03514342060651483, -3.825195132451639e-05, 2.319549644050104e-08, -5.754601021054693e-12, -14128.379102977597, 1.982806836885361], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.745137086884194, -0.011132962587886342, 1.9585105275320877e-05, -1.022169441323885e-08, 1.8010342925635519e-12, -17726.917856363652, -70.19617753909878], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.7253409244789397, 0.014265181170639244, -2.2141036425093912e-05, 1.715977168377431e-08, -5.148141592865579e-12, -10262.389555752692, -5.8800571706788265], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.853405311079901, -0.0020628194416833037, 3.5777099227838903e-06, -1.8218829904511497e-09, 3.1470295920366487e-13, -11146.524327342462, -25.965581204091627], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8461526291075379, 0.030516791280725722, -4.1881736602276666e-05, 3.038458802712859e-08, -8.77241924472142e-12, 8892.833885625414, 1.700633417777759], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.071578543818658, -0.006359519644350275, 1.122398548687906e-05, -5.882501528205005e-09, 1.0398332318213258e-12, 6507.977963925237, -48.97468981126842], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.9579285228368597, 0.03417772791769032, 2.8267220648699003e-06, -2.457698177049797e-08, 1.1560069899609181e-11, -3869.2198522316385, 2.1103754351703756], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[24.884340014131855, -0.025217720437181054, 4.491339708311578e-05, -2.3913101465419666e-08, 4.278551439861367e-12, -10836.46522315959, -123.21622282526225], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.5564370461873773, 0.024881903355254725, -3.188390767026589e-05, 2.1907635272799272e-08, -6.062373544127778e-12, 10135.826893224556, -4.0963725142147105], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.380928480069938, -0.005719365098309717, 1.009788869879846e-05, -5.296770422021596e-09, 9.370128013106177e-13, 8019.261717720301, -48.12514088667], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.4610643361458545, 0.025330937651535084, -2.952442486932989e-06, -1.2660199484314385e-08, 6.611412080923329e-12, -24805.098009136753, 3.4586306168646175], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.750183996525017, -0.016155448096907526, 2.8860319423811855e-05, -1.5435830592843934e-08, 2.7715473667714806e-12, -29493.398045580136, -81.59744036597324], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.36992005380184995, 0.028658553459045617, -2.7893650477070972e-05, 1.365264345505228e-08, -2.5391260047595702e-12, -30533.3454375843, -0.3700132312478832], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.223394933664462, -0.007741656718226097, 1.3941833379523655e-05, -7.541925855989244e-09, 1.366694747096425e-12, -33614.39833695342, -60.680047408876725], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.5846710296946194, 0.021387565980468766, -2.6680173457627973e-05, 1.8085999289419217e-08, -4.9546828517619085e-12, -7436.838079350493, -8.566469520709774], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.40654432318191, -0.00539963874156887, 9.490941400863514e-06, -4.944501452456702e-09, 8.700344601728661e-13, -9329.465574900769, -47.67575450989249], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.2803796894037913, 0.02614640142738547, -3.3204738620197315e-05, 2.17354976395738e-08, -5.739491001152499e-12, -14128.2002322002, -6.266953809472011], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.200433121117815, -0.004387978314767232, 7.853842788245606e-06, -4.205148239053619e-09, 7.568997794706727e-13, -16281.374282119961, -50.85662668887936], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.6873624979846867, 0.02132348587051325, -2.3360423647016946e-05, 1.4597562040876269e-08, -3.850954977215968e-12, 5488.966504681735, -4.107438891922268], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.374614883023785, -0.006606541562999505, 1.179735866599913e-05, -6.2973629228668596e-09, 1.128962721984746e-12, 3275.2147664892946, -48.04572057440734], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.7274687151788672, 0.049119357377887446, -5.721657999929561e-05, 3.620716070238383e-08, -9.375816653272977e-12, 1266.5062745649554, 9.215098033048262], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.965381125832987, -0.012665119421307415, 2.2613287770754012e-05, -1.2071207364431159e-08, 2.164310601675397e-12, -3382.494524485268, -84.83323367938382], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.14058757860282445, 0.0339593145441138, -4.877974346793553e-05, 3.545526738280943e-08, -1.0228438823198347e-11, 16315.888986273174, -0.9856408051883303], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.244766688874416, -0.004423018106424232, 7.94050099726946e-06, -4.265908347437528e-09, 7.694708249044139e-13, 13945.66489193781, -52.212001654461716], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.1548843096330083, 0.024665053123515933, -2.7882933372644482e-05, 1.674351734080543e-08, -4.172550802331409e-12, -17579.595194694375, 5.361958269400905], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.176483494605419, -0.005390085960629095, 9.767411090315341e-06, -5.327185556465479e-09, 9.71578911886277e-13, -19944.658496372707, -41.79601155058337], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.2813895297009909, 0.023606108580225396, -3.32958999415923e-05, 2.359375866261309e-08, -6.5998806242871875e-12, -26338.947226823897, -2.8493646381442304], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.5727769500641555, -0.0031657845857092286, 5.618119269741751e-06, -2.968319410170091e-09, 5.286839827333997e-13, -28000.921204539423, -38.82971614948833], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8975799898301388, 0.024674325054387276, -3.7013627254013554e-05, 2.820733239221419e-08, -8.568603144806883e-12, -12291.197588980347, -4.673117509058805], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.17818491600952, -0.002748730322506742, 5.0529761150264075e-06, -2.80344987594243e-09, 5.180262050244086e-13, -13947.106252653144, -40.510730844422696], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.680794872389105, 0.031212634423942055, -8.078943332836512e-06, -1.0837702535713005e-08, 6.4822065381566345e-12, -42938.96019157139, -5.807840673061104], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[20.413219230004987, -0.017360182930587425, 3.107644830157294e-05, -1.6671325208916026e-08, 3.00083057386381e-12, -48282.09222223303, -103.39683749805015], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.0356460517609796, 0.024037644863322157, -3.107154442970579e-05, 2.127465910347592e-08, -5.936338916055722e-12, -17011.574868367785, 0.8423575722048966], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.320908348369045, -0.004524717722003204, 8.146707072951768e-06, -4.398961272374802e-09, 7.961302458547478e-13, -19016.495111618435, -40.56221379280525], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.5632758919585985, 0.014266198380516518, -1.297395417218e-05, 7.268783904885332e-09, -1.6907465693521607e-12, -15060.266506077436, -4.452591958023614], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.417079534292768, -0.007111067690577012, 1.2402771045542844e-05, -6.3880652311414095e-09, 1.1128397777111e-12, -16830.85050417842, -39.256700328655924], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.7671501926646207, 0.004179533631941145, -5.164607743638101e-06, 4.281739579109777e-09, -1.5327069879359516e-12, 12122.479330228, -16.44866513851015], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.522342266148612, -0.0014872427813327454, 2.711546949928347e-06, -1.4880463699830897e-09, 2.725086073803661e-13, 11656.693933735425, -25.372445299054252], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.5872221349012045, 0.021884270599099157, -9.092121797012328e-06, -3.2012964852407535e-09, 2.9345614276199e-12, -4861.96701838162, -3.0977138605766337], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.083473779701674, -0.01198298477007132, 2.1302933514614128e-05, -1.130980789728262e-08, 2.0190212524053155e-12, -8346.040194418949, -67.81731223292809], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.5697161361949867, 0.02688818075889117, -2.5056284180623917e-05, 1.146336855720521e-08, -1.867258641769468e-12, -26386.69968704882, -3.354236050343962], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.974045935513386, -0.007721478316922923, 1.3817672610535578e-05, -7.4052216195143655e-09, 1.33270402028631e-12, -29367.030533744597, -61.470335351211986], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.50070887996909, 0.020387521081802598, -1.8341243242455437e-05, 8.052130964312552e-09, -1.1760149275079393e-12, -23313.133742896443, 7.422656035871933], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.40355860509355, -0.006564518653398889, 1.1718367467161162e-05, -6.258471900887298e-09, 1.12274947821416e-12, -25643.353761741666, -37.96810045550923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.17029024801610773, 0.0268182450445098, -2.118802075257814e-05, 8.20992879089674e-09, -1.0277651826883892e-12, 5547.584904329878, 4.199457412783353], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.950283389141536, -0.010553854796415922, 1.889093754738386e-05, -1.012621653934156e-08, 1.8215285473882093e-12, 2108.166503557566, -61.34926197134298], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.1585581863369327, 0.024854007498684647, 1.5352589861863806e-05, -3.2530236035268404e-08, 1.3506761347584495e-11, -22561.107666381675, -8.741377463172444], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.283228357038233, -0.024540691481903347, 4.373133656386623e-05, -2.3303694764893882e-08, 4.171502185094242e-12, -28887.594065885365, -120.20180268817303], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.729799321094273, 0.04774875974020035, -4.5782720231629656e-05, 2.3451902359183242e-08, -4.784878137047558e-12, -9365.579502232267, 9.23473895211129], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.856640051434304, -0.015730966508547484, 2.8107689274754105e-05, -1.502763849849372e-08, 2.6975400904649e-12, -14718.890683598103, -95.48091574101521], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.876498538219424, 0.050410961179657245, -4.037089364111962e-05, 1.4788252070062394e-08, -1.2397132463947148e-12, -12094.557906245042, 15.749957186446128], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.660127704274004, -0.018925442308153313, 3.3821160292992076e-05, -1.8093152908561352e-08, 3.249415043434457e-12, -18371.141462846994, -104.75673421506201], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.3727155297520173, 0.011948614721576689, 2.7150442893396317e-05, -3.885262821261e-08, 1.4940585792720143e-11, -31095.273264142248, -7.758943923505084], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.516662011189382, -0.019074667402888438, 3.401223628625084e-05, -1.8145941051450386e-08, 3.251440881733763e-12, -35853.68595572452, -88.7571775732124], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.25359747125502013, 0.03316645059515096, -4.2635363743570896e-05, 2.8610013767743077e-08, -7.693956409845132e-12, -20564.392376735625, 5.808127430174561], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.171428937865954, -0.006471958666490914, 1.148563702969594e-05, -6.073125879012102e-09, 1.081565316164111e-12, -23294.86717963766, -51.16808406751664], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.3443421445817303, 0.04526677297402831, -3.344769958431689e-05, 1.0361238140271254e-08, -1.3049751954688255e-13, -15477.226706177851, 8.41337917748708], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.655419044313952, -0.018621890585014664, 3.322656264203289e-05, -1.7733435491462823e-08, 3.1788162559847158e-12, -21395.604538174768, -104.46649209889019], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.230071397663444, 0.02922230492068527, -4.331550102355607e-05, 3.3142820009992894e-08, -9.964716603519656e-12, -626.7608393507137, 8.30175060971999], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.834593051930907, -0.005149254345543626, 9.154900952399453e-06, -4.8491696136799125e-09, 8.637658608321683e-13, -2663.4787347679558, -36.22149889077965], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.04254935440883842, 0.027932823795898315, -3.942775135867983e-05, 2.937991628387392e-08, -8.786789264602963e-12, -10082.468208058068, 4.03640870027108], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.117733506574382, -0.005002050286644842, 8.996340998406024e-06, -4.846541563089684e-09, 8.752661556523988e-13, -12207.376060290822, -40.93660920332789], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.9848871326035258, 0.03601483344827752, -5.0652436068441856e-05, 3.628432243992061e-08, -1.0380463210322537e-11, 26973.20102018257, 1.6647093356298557], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.257823446292662, -0.0048651367784269565, 8.797725025607717e-06, -4.777700946316846e-09, 8.686587296736319e-13, 24369.436648515562, -53.96723369238215], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.4987376583938574, 0.020575203329311727, -1.2687807227592196e-05, 2.0580218649546865e-09, 8.052493799963351e-13, -3245.3605878577328, -3.116352064255457], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.222910672801934, -0.009612822436863976, 1.7159491347730213e-05, -9.163523736890461e-09, 1.643349158286699e-12, -6186.8537994822145, -58.400948082693645], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.366212466475686, 0.019020755329734976, -2.6531539297715955e-05, 1.901896765411244e-08, -5.525648718992467e-12, 9332.95320120936, -10.664663135943652], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.334162438965064, -0.002320014384334396, 4.27361527366728e-06, -2.380223420103809e-09, 4.4120752542054135e-13, 7923.429748298386, -40.31025900442854], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.6717552649086471, 0.024196114205772633, -3.0224133412150824e-05, 1.9895414249105653e-08, -5.3401890565958715e-12, -21112.8665572529, -7.690249213748317], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.180353531463835, -0.004638294019722697, 8.319828024271381e-06, -4.468738796550366e-09, 8.05812511578085e-13, -23190.40990875528, -50.318252342490425], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.19305972258692997, 0.028838444208012237, -1.1311643252938327e-05, -5.046714820348226e-09, 4.143908328919645e-12, -3191.171920982836, 4.760705180598958], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.77750346417998, -0.015741210151712794, 2.8070455953176596e-05, -1.497215425395219e-08, 2.6824591745406734e-12, -7839.505195474895, -81.23812676790907], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.29447758737461366, 0.014416268368780336, -2.6132274716597896e-05, 2.19005960702076e-08, -6.980197262178007e-12, -13066.562285947317, -0.1994364663449193], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.902441066530188, -0.00033857631003595914, 6.433642615608704e-07, -3.663229139884261e-10, 6.900876877074478e-14, -13654.383053304307, -15.255938164267217], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.2303812875933364, 0.021364197591551247, -1.0987964053318556e-05, -4.0854759822882103e-10, 1.7279200745627597e-12, -32282.401311062615, 0.4124679531891413], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.896110212786931, -0.010602930836050555, 1.8955766424558903e-05, -1.014588758269268e-08, 1.8229290835573665e-12, -35530.476320764086, -59.95424168175581], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.9435117412246647, 0.019776748061822925, -3.3633669965892776e-05, 2.69027205608612e-08, -8.279588621352525e-12, 8836.270428209267, 7.174711632768557], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.8134790637397984, -0.0006939624330756862, 1.3030903022972307e-06, -7.38705282440372e-10, 1.3879664369318713e-13, 7895.727522447026, -15.57387405331816], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.009596244858614, 0.013359762089486851, -1.6230395188513717e-05, 1.1002958821921981e-08, -3.144849384765542e-12, -48891.55547144392, -2.5929267513391157], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[6.982981854268909, -0.003098712112713326, 5.6288267144297645e-06, -3.0784726583392297e-09, 5.624487853420682e-13, -50143.21304469151, -27.65200824753493], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.864064029783179, 0.0007534567621938237, -1.6557146443906212e-06, 1.5522321845571488e-09, -4.4678199899427846e-13, -3929.484853353702, -8.85806483523984], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.068797059263744, -0.0004958074785788374, 6.592350997545732e-07, -1.7259805793240392e-10, 7.629710642176063e-15, -3940.910458467904, -9.719180644962087], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.997163459676221, 0.025096367875411075, 1.3273981270537233e-05, -3.2292476608538905e-08, 1.3906144966522682e-11, -4427.7643616402875, -7.722032869612473], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[23.93148816741965, -0.020915959681285554, 3.737406290573611e-05, -2.0002143005338437e-08, 3.5937325770765385e-12, -10399.386759012588, -112.97985763374597], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.2231431046088153, 0.01834145979288753, -3.038634051719904e-05, 2.3891593837292015e-08, -7.2681380168047015e-12, -7574.588250250176, -5.827717145830172], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.792957355107627, -0.000775278020373442, 1.4507039279134061e-06, -8.206168955010979e-10, 1.5395183363812744e-13, -8504.747029379607, -27.814778952989386], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.2298213432217238, 0.02857063804125655, -1.496333096725277e-05, -5.176144688234251e-10, 2.3810124389470935e-12, -2062.3713241674186, -3.8813822966699973], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.662164907289366, -0.013767036681277524, 2.4610325704575188e-05, -1.317144779378733e-08, 2.3665202505494713e-12, -6350.739648656845, -83.71182114305013], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3799277144153752, 0.017751048374544384, -1.2085009646792297e-05, 2.5391485883052004e-09, 6.810061003660516e-13, -12454.535457958238, -0.2827546322895884], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.249398692011312, -0.007938517464891128, 1.394200118309795e-05, -7.265191809821805e-09, 1.2784305304423827e-12, -14823.293578950015, -45.75607181654314], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.671928380296754, 0.03806453544601215, -3.824364034033048e-05, 2.0402333100490047e-08, -4.2892849768500005e-12, -9344.348999242991, 10.504117350751589], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.22900797879716, -0.011870677654334062, 2.11521841314246e-05, -1.1264170391874369e-08, 2.0156707850116316e-12, -13420.652244696717, -70.11909663641367], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.9695826145588105, 0.020522910467802736, -1.1621303537285643e-05, 6.215947121188319e-10, 1.3989988265619881e-12, -30660.778518958195, -2.354813787499431], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.866079513329586, -0.009800423892010647, 1.7404572685183046e-05, -9.223255361972795e-09, 1.6448101392275288e-12, -33658.8500559887, -58.594587650619204], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.928547982226252, 0.055347224152330024, -7.064619241191545e-05, 4.678540699667859e-08, -1.2437677666673803e-11, 5292.949773035705, 18.28104899467152], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.083440579108537, -0.010265272318696563, 1.8411704037878588e-05, -9.893058752235126e-09, 1.7833995421376626e-12, 726.644959415662, -76.6280144936056], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8730945145744824, 0.01932591651963461, -2.4337288058073702e-05, 1.6132669529287834e-08, -4.3452685233347906e-12, -20446.61949648703, -2.940430061881125], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.634552929378818, -0.00373565753306562, 6.726647908112743e-06, -3.634375865529283e-09, 6.579565431917768e-13, -22090.819871604435, -36.77911518578289], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.057365593707134, 0.018785524577517754, -2.938071828696827e-05, 2.3501879626712106e-08, -7.340233774627739e-12, 1799.1466616377027, -10.421533427695135], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.609520992494424, -0.002985913866322768, 5.278296555000554e-06, -2.7673936978931187e-09, 4.893077530618933e-13, 581.1155630611138, -37.53349411092843], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.325697207973752, 0.052276209808796874, -6.524821177224823e-05, 4.254893570548873e-08, -1.1179374992415796e-11, 2784.160615160395, 15.786103875881018], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.035499648684327, -0.010328872436853105, 1.85144275765406e-05, -9.939823448763025e-09, 1.7906302020390325e-12, -1667.1861519303275, -76.07103631506996], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.338354442903763, 0.054935658346410024, -8.043484188784984e-05, 5.942975881630762e-08, -1.7339191803730213e-11, 12568.267830923005, 15.17531455869554], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.219609316633798, -0.007225593312563003, 1.2980724661474071e-05, -6.981190875436321e-09, 1.259479238125277e-12, 8835.410932328874, -66.26226315601645], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[4.854963190191201, -0.005541352146191829, 3.011981211984818e-05, -2.992259178960762e-08, 1.0050251495844049e-11, -14354.343236663533, -9.256212644947741], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.541393802389278, -0.010402513459215392, 1.8377740057320232e-05, -9.667651326969172e-09, 1.712113796559036e-12, -16092.27674730979, -35.56384349771318], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.0296505618963183, 0.030564388351008547, -2.573339947448623e-05, 1.1293814582996451e-08, -1.8218102198128518e-12, -6451.163800184483, 2.661800407957176], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.238947633456396, -0.012066243521202133, 2.1530927686058267e-05, -1.1489308805950374e-08, 2.0590196854474402e-12, -10239.60691342871, -70.2795488210599], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.654522187759569, 0.015399204618219127, -1.0183843920249032e-05, 1.7530408697863282e-09, 5.796142718035787e-13, -38399.498068624336, -11.08112248928635], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.183628084500272, -0.0054815561428007975, 9.935047020584658e-06, -5.424764871503284e-09, 9.90183936538719e-13, -40482.1830627576, -49.97906870532997], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.2647794270171597, 0.030351793367030033, -2.0473808973331654e-05, 4.470368545264202e-09, 8.498142387679998e-13, -32512.740720895657, 6.533217326591428], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.898907986176589, -0.012891086688642686, 2.299990260511306e-05, -1.2274830910706834e-08, 2.2004947587732965e-12, -36630.06153907625, -71.46373716229328], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.2534252592930923, 0.03273023230971289, -3.7549336347651624e-05, 2.3211474977732365e-08, -5.930848056387698e-12, -14127.15157149639, 9.926635513532794], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.179450910712191, -0.0077980928248902875, 1.4043712561806583e-05, -7.591809088068108e-09, 1.3748360645524598e-12, -17253.863951757397, -52.78348947784657], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.158935515063618, 0.03704251468301276, -3.123325289305005e-05, 1.299532108851229e-08, -1.8017602107366419e-12, -7290.124014882366, 2.959115564892998], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.804654358443338, -0.013393436414739883, 2.3947520166646413e-05, -1.2818034648818227e-08, 2.3031836911431005e-12, -11796.97920545514, -83.79743142943462], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.3606812055829094, 0.014165741119406038, -1.8920034876906727e-05, 1.3801135001197637e-08, -4.178697974398651e-12, 5624.946356042613, -5.695726443073275], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.2138098621097955, -0.0025695692655428436, 4.704895113594066e-06, -2.598842889969052e-09, 4.785316546892411e-13, 4433.044775463999, -29.994754260294286], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.9288908469196022, 0.01631863837581355, 6.612707436873752e-06, -1.790283949866309e-08, 7.848203527005099e-12, -16303.104806600682, 1.6939949071612705], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.774417869034094, -0.014595526992164157, 2.584779642414162e-05, -1.364659883617138e-08, 2.4255122231087387e-12, -20082.767378659264, -65.80621537833719], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.13128416112695, 0.018402879969436646, -2.427790252895168e-05, 1.7224366790096025e-08, -4.97078537901173e-12, 16308.708626109817, -5.779500557674478], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.494135186661154, -0.0037972448834479857, 6.797285997298148e-06, -3.6381810422527367e-09, 6.538477544376298e-13, 14778.234182998638, -37.52196340150498], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.8633034847803445, 0.00447274134417627, -7.657893264373758e-06, 7.56655396753431e-09, -2.8240306758178458e-12, 2100.92849892217, -7.401141450695354], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.411397333558405, -0.0016031848947045287, 2.888008716702244e-06, -1.5563243370502838e-09, 2.807780377934843e-13, 1735.2549426497226, -15.027262402150276], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.57393752382407, 0.04773994433496034, -4.598075902632074e-05, 2.3513577988467583e-08, -4.74549935705454e-12, -8370.226345852034, 9.441573771652568], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.90804583938127, -0.01554928042668577, 2.7772972432876872e-05, -1.4841545994282823e-08, 2.6631345649390127e-12, -13685.120270011297, -94.69771305042104], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.2993590289976177, 0.03629507505554338, -3.944363019386016e-05, 2.3073417087596162e-08, -5.5051741108559596e-12, -12642.136403759114, -0.5242651314860174], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.089049634499672, -0.009905139055121031, 1.7696124240999526e-05, -9.456997661392868e-09, 1.6972916504405012e-12, -16284.912288556126, -73.24267899700494], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.465893494328092, 0.040326742804508854, -5.167768077838933e-05, 3.378400977387666e-08, -8.785376186660027e-12, 12181.427581042497, 4.137161831354298], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.15817082968341, -0.006887695723303913, 1.228645402794296e-05, -6.548938302997464e-09, 1.1738112876830724e-12, 8934.603776509859, -63.78765014234281], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.336002996485873, 0.0409549712056197, -3.308969192793541e-05, 1.2340897201466682e-08, -1.0794828237206684e-12, -4231.746092212201, 14.860392314439837], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.749750232948465, -0.015545077687185656, 2.7694700812801267e-05, -1.474786410170757e-08, 2.639181402087929e-12, -9300.48164152424, -82.77154674249263], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.1382095149591014, 0.0282308858589733, -3.843757277652183e-05, 2.6868220618134602e-08, -7.519333579859374e-12, -13762.759588064393, -5.6223179121642595], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.261943194125891, -0.004316960996473441, 7.734084101523613e-06, -4.1449098034160916e-09, 7.462531399258285e-13, -15902.956870758993, -50.91350552146117], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3347756970000422, 0.024001944929553876, -2.5656192715494082e-05, 1.4867701069805415e-08, -3.529700979146314e-12, -30934.050864571604, -0.6581568991046858], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.997091214982685, -0.0067959560913868, 1.2045689549684656e-05, -6.359630560617082e-09, 1.1313338890554778e-12, -33390.084026511555, -49.545589544198634], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.376886249031483, 0.017168302158811342, 1.0226301911290717e-05, -2.3112237422527253e-08, 9.759452808223773e-12, -48291.4127099092, -7.590703434367445], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.381507855457443, -0.014838932726415921, 2.6561063767874826e-05, -1.4250111465226413e-08, 2.565178273140125e-12, -52514.014074891384, -81.64682166136448], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.4985899067737747, 0.03235521512552531, -2.157189765044062e-05, 4.167243773143873e-09, 1.189220221740312e-12, -1408.5020007541907, -0.5266536594811804], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.602521998224887, -0.013353262510873848, 2.379895972007314e-05, -1.2680916803721156e-08, 2.2710689730396306e-12, -5786.144003553916, -83.4000352876333], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3860228690548224, 0.01664180070958826, -1.691944848682036e-05, 9.530145472170789e-09, -2.1792604911653112e-12, -4007.991528370623, -0.7177164604384512], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.443713882410815, -0.005684030598010781, 1.0035176681229939e-05, -5.2677814920604205e-09, 9.32181599258653e-13, -5810.448620970849, -36.467218292994794], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.9328990041902597, 0.025594416441077662, -2.992923842063736e-05, 1.7922510788053372e-08, -4.3129092664097374e-12, 7182.597001986232, -4.323548803376326], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.189899521001854, -0.004837262777332801, 8.704529743823447e-06, -4.700779187954059e-09, 8.512912467357585e-13, 4886.495764265692, -50.903801324359165], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.909339257180611, 0.015109869204267344, -2.0359935894131893e-05, 1.4975414475927186e-08, -4.539495935412317e-12, -12913.267567461682, -3.189178505591901], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.0796245419535895, -0.002883572108895685, 5.257875948923466e-06, -2.8882221856448178e-09, 5.294849114943783e-13, -14173.989813993268, -29.03240824156009], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.3537168320081558, 0.027380497214718674, -3.861263541683069e-05, 2.9270145806938097e-08, -8.860747020350934e-12, 13994.313406765697, -2.856802582598279], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.507386199331888, -0.005965214859330341, 1.0615013047056207e-05, -5.6303433478661636e-09, 1.0041363772917085e-12, 11856.429531010046, -48.1889470991562], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.2710400479545125, 0.042753919623597, -5.6165265498022976e-05, 3.844193026667482e-08, -1.0600420168224058e-11, 16249.424017500096, 6.93065379542832], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.129040622997985, -0.0075721888366530946, 1.3601585797108142e-05, -7.320888786774163e-09, 1.3215753793914062e-12, 12813.086132134762, -64.82512253351541], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.528087055181124, 0.02857834721648984, -2.223493897999984e-05, 7.78829680004498e-09, -5.933623265363172e-13, -22437.33404386304, 7.519459865290672], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.978148363086962, -0.010727802631054727, 1.923681044853637e-05, -1.0341449654840112e-08, 1.8645491290890467e-12, -26073.55669194138, -61.77926305676107], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.861978139702, 0.012267712827676622, -1.7731771898190192e-05, 1.3155375661569419e-08, -3.940110211157303e-12, -6275.99064823019, -9.289679054876098], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.603255701316299, -0.0013940149474614871, 2.573609745219915e-06, -1.4363138871988452e-09, 2.6664790772466233e-13, -7148.294106663131, -27.81226494128604], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.3594895290935365, 0.026577920029637908, 4.854347893811019e-06, -2.3300735564299874e-08, 1.080240452560062e-11, -52590.397742976675, -2.7290661309693327], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.248869847069475, -0.019320918938579023, 3.4415805860354394e-05, -1.8332023497245443e-08, 3.281693142243804e-12, -58122.213639117515, -101.87023226406923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.2607884856984228, 0.029660041183224028, -3.746241988003589e-05, 2.3585704709074063e-08, -5.9791502980121475e-12, -55608.20717342562, 4.317566625811727], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.046792119421534, -0.0035163837471446748, 6.491774135131538e-06, -3.63351596817553e-09, 6.762976607156029e-13, -57983.68076945334, -44.673212142991225], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.3891834425750581, 0.029211277410396207, -3.686306151947091e-05, 2.577720747368924e-08, -7.388351945821803e-12, -18013.439597681838, 3.258481265545784], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.099152696179464, -0.00740803758014022, 1.3248009828239301e-05, -7.0846351626462554e-09, 1.271765079735496e-12, -20634.004551282353, -50.37066777803927], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.6898519796340031, 0.011560723280555569, -1.817207466966703e-05, 1.4019490013326949e-08, -4.134118961468191e-12, -18153.376774706583, 2.129079946916434], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[3.959399298266145, -0.0016598677646833847, 2.8312663882910362e-06, -1.4039369865093347e-09, 2.370107070168396e-13, -18832.111440443205, -13.688872370829205], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.11893124833978236, 0.025418106629255515, -9.60813723896004e-06, -4.295184920885645e-09, 3.4643578480313606e-12, -12617.29593360906, -0.7380431667168059], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.060759437781124, -0.014857617902346767, 2.646305942786631e-05, -1.4088105047881865e-08, 2.519977650362168e-12, -16807.888008241818, -78.2120077633692], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.45569245573642814, 0.026371170970668587, -2.119315323144256e-05, 8.246547427954872e-09, -8.510583322022998e-13, -9619.360148651629, 6.940776949993572], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.091021176024213, -0.011033050657229601, 1.948440782141599e-05, -1.0237438997912486e-08, 1.8128750369440557e-12, -12934.940051445123, -57.16806380587336], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.9935249972872466, 0.019188099593394046, -2.429251893386779e-05, 1.547806119453079e-08, -3.999510495247158e-12, -12323.709272889744, 1.4914047355837052], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.3549857194819666, -0.002362712934473869, 4.361156004630767e-06, -2.4396412345899768e-09, 4.538688010482443e-13, -13872.238962628915, -30.368811439276016], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.7686503489171215, 0.01542091036029991, 5.7678671325625765e-06, -1.5827036114196573e-08, 6.751805874198409e-12, -27533.95117046811, -5.059374506169936], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.847750289631566, -0.013358196437016788, 2.3868930992592283e-05, -1.2769340494758564e-08, 2.293053251332945e-12, -31129.859046153855, -68.67480973712077], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.3310333521335915, 0.024146766279956305, -3.506378568590779e-05, 2.529021162187046e-08, -7.269035813588719e-12, 15092.726586779507, -6.608641604265827], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.420679967326969, -0.002119675924606964, 3.923915474448427e-06, -2.199549269866415e-09, 4.0981950716182524e-13, 13477.069845866472, -41.56605401170923], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.4414138418118525, 0.020141859424894347, 1.0044446840284764e-05, -2.463246133813414e-08, 1.0643657854156933e-11, -32356.641014465564, -2.1625230684937087], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[18.59927922849303, -0.017944234862440914, 3.188095317172687e-05, -1.6915790412408206e-08, 3.018709497642978e-12, -37154.47276142184, -87.27524842158932], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8242890383969044, 0.02601751304184486, -3.764246912888286e-05, 2.8538893768921333e-08, -8.616190420976025e-12, 16315.132340127682, 0.7718530492042515], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.101367827021647, -0.00456807440908673, 8.155002280320334e-06, -4.3442101951809755e-09, 7.779507962299416e-13, 14406.971221485384, -40.10483055074011], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.2307503242913636, 0.017783672033410882, -5.881554623577392e-06, -3.7124054481140603e-09, 2.534903429637312e-12, 10544.600870403421, -3.175200465880055], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.925749627491374, -0.010525830849765385, 1.881401646140625e-05, -1.0066604762756274e-08, 1.8080352392721393e-12, 7506.419447197253, -58.7921375347804], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.727377095912076, 0.010788742384813208, 4.996702195606158e-06, -1.246812163894486e-08, 5.318864803343917e-12, -18875.02857982935, -1.535189245856838], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.340293489956832, -0.009501601267967775, 1.6974032581442658e-05, -9.079342159244687e-09, 1.630182196543473e-12, -21444.67495799407, -46.9368519825885], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
The two lowest frequencies, 51.1 and 54.5,where replaced by the 2D gas model.
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
            NASAPolynomial(coeffs=[-0.09381182056884507, 0.03254187222991623, -1.9508110350787407e-05, 1.9033782508869717e-09, 2.0178446452117993e-12, -34082.08616685792, 5.477455046706972], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.82361115978394, -0.015032597046991501, 2.673267355141984e-05, -1.4198360355959291e-08, 2.5358456464057607e-12, -38704.03469135315, -81.692139574811], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.093289887828344, 0.04054760133267703, -5.061871732705487e-05, 3.338410158590412e-08, -8.850737602838465e-12, -541.4482127858287, 11.044520821165023], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.340388622067284, -0.008856585729731317, 1.576723580322424e-05, -8.379513537761487e-09, 1.497432943060751e-12, -4030.414563167098, -61.114425198681666], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.845869772045593, 0.029847060312587794, -1.628809354174271e-05, -5.160491965704225e-10, 2.710703137359879e-12, -2142.4301922694967, -2.261969514766644], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.5641311262753, -0.013464308948140019, 2.3999166551477703e-05, -1.2790803986637513e-08, 2.2913057407046566e-12, -6481.525437027618, -83.47569886756405], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.8122454662822548, 0.022408186687580628, -2.560543453034468e-05, 1.57371471116863e-08, -3.913545531509474e-12, 14152.973360680855, -4.91399191411749], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.420918707722631, -0.005908517541909402, 1.0467891713363109e-05, -5.523248385183462e-09, 9.815547097021576e-13, 12014.28897872468, -48.237535396419695], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.3179759634926335, 0.0337808413581288, -1.4799644205232365e-05, -3.8491413884411814e-09, 3.936376563027633e-12, -33918.12397377484, 3.5720153927481775], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.33780516505024, -0.017434388906007334, 3.1197672701430394e-05, -1.672266359942932e-08, 3.0079829299315474e-12, -39258.717732785706, -95.07246589024183], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.87254397088662, 0.05562115022908753, -6.411747077035248e-05, 3.909467124911917e-08, -9.649869180968192e-12, 6941.620454901263, 18.428549148356694], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[16.033249710332335, -0.013087049609188788, 2.3459276973037306e-05, -1.259971499506201e-08, 2.270175476880566e-12, 1737.2650744994153, -86.81228063088199], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.8969894204316542, 0.03136539693889586, -3.4536644563109175e-05, 1.9380379723494867e-08, -4.2507509773707146e-12, -71446.19200022392, -0.68218822580506], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.83414653439374, -0.007126662868102691, 1.2639025393600533e-05, -6.681789222829951e-09, 1.1906507052808577e-12, -74435.28062953908, -60.909884239060105], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.2528271717823889, 0.021960853072192966, -2.9950805254072694e-05, 2.1358406495852024e-08, -6.125744278389399e-12, 13593.483465300698, -2.722569916258606], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.479259361045889, -0.003801898301520045, 6.806694342146216e-06, -3.6435494737371158e-09, 6.550312794303392e-13, 11890.260978320735, -38.61820201050499], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.6497200202396973, 0.03554662728230054, -4.414273761871482e-05, 2.9390380325897868e-08, -8.001764887509263e-12, -26238.76838900594, 1.807716989089589], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.113684459562291, -0.007677001309484304, 1.378788122493188e-05, -7.421196343832306e-09, 1.3394170505570683e-12, -29365.907074311795, -62.16520844202522], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.41437160158067576, 0.029786648072623385, -2.4261111177433176e-05, 8.221458673271484e-09, -2.8178432574192725e-13, -25626.634220050415, 7.219095577642271], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.025015415395226, -0.009793662387205191, 1.746096735571733e-05, -9.310411480084661e-09, 1.6689307373163845e-12, -29190.40099243482, -61.54135188988288], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.01004470369341498, 0.02791597303053718, -3.700810576004676e-05, 2.5702915657357916e-08, -7.117883280758288e-12, -6799.958705226383, -1.4839040687912517], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.464334209792526, -0.005614606678231816, 9.924579155785779e-06, -5.21537157585454e-09, 9.23919831904687e-13, -9032.064883834817, -48.57071280640966], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.4051553239077674, 0.04772432624434403, -6.435604590351414e-05, 4.4498007855471054e-08, -1.2296018776289625e-11, 13932.5552575459, 11.836372705741438], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.13485602704688, -0.007526899326676363, 1.3520521427517482e-05, -7.277188858920366e-09, 1.3138248271359224e-12, 10281.131373003658, -65.34134282981252], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.3776185830032743, 0.03725661522186618, -5.301687366404207e-05, 3.855551373436394e-08, -1.1193466147629879e-11, -21030.518808455352, 3.9623145076094723], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.19884335333455, -0.005117164491241796, 9.26393185218533e-06, -5.03839716544939e-09, 9.169570127262039e-13, -23703.966300766202, -53.26797674688753], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.923559650403525, 0.010682167427457987, -1.2508207230245296e-05, 8.481356257219259e-09, -2.479574666310336e-12, 6451.526356036324, -2.1766933077174144], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.086218027664706, -0.002805163944210358, 5.098963197031399e-06, -2.790912944385265e-09, 5.10197102424659e-13, 5383.5898021712155, -23.2375924047948], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.002420863527872, 0.052218930509092, -5.8912220017090593e-05, 3.5103579582651726e-08, -8.419351287482174e-12, -1583.845967155803, 15.082242057734835], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.94864942503676, -0.012883704040235191, 2.3028300934389553e-05, -1.2316747773961674e-08, 2.212019378413639e-12, -6568.298258909366, -85.4535618567902], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.2454370584641636, 0.04574074806029313, -5.206793518635491e-05, 3.101160852399004e-08, -7.43118459955382e-12, 6383.047798987318, 14.227558962570399], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.973716155667459, -0.0105202866705927, 1.8851670215405163e-05, -1.0120414494181442e-08, 1.8231145336117972e-12, 2086.6894109549958, -72.51980596584465], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.3004211190936877, 0.03619618378400812, -4.288433116141816e-05, 2.7141716545675755e-08, -6.9348514635331996e-12, -19065.39671340276, 5.4836795586656235], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.191111192077285, -0.008864303910011589, 1.5729139707727176e-05, -8.318776955266876e-09, 1.4811265511128364e-12, -22382.581028305867, -62.242601729283976], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.3590481876570226, 0.025017264849508964, -3.095876012163775e-05, 2.0028701761671274e-08, -5.265201954870357e-12, -50225.62514884256, 3.527368427308401], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.16265459163228, -0.0047014713090986066, 8.435565210398846e-06, -4.533667902508682e-09, 8.179721319053217e-13, -52377.34765216971, -40.59755365821063], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.2669663874304872, 0.02565872777984169, -3.674611809733618e-05, 2.652569807598397e-08, -7.566881524298349e-12, -856.8766902884887, -0.5998718035367387], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.589729576992117, -0.003442805844755854, 6.154114514875651e-06, -3.286433935095303e-09, 5.89855534744033e-13, -2641.1977888549245, -39.32239443637718], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.4844916391592626, 0.04961192793921256, -4.65420378199895e-05, 2.2377955292019276e-08, -4.031096664750873e-12, 950.227407630915, 13.750587386873498], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.886822640780572, -0.015838521517526086, 2.832517482302733e-05, -1.5167314972714757e-08, 2.7260961337651463e-12, -4616.72068513157, -95.03458662532132], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.026357597560027, 0.05033086334280123, -5.385886813444802e-05, 3.03407714566931e-08, -6.849186072837592e-12, -812.6325351185028, 15.773821367616957], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.896372667746718, -0.013266240808539003, 2.3747349222037652e-05, -1.273077201589351e-08, 2.2905139292968324e-12, -5865.603975863925, -84.98127216420023], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.4037608521331618, 0.03434776419035948, -1.5893400945502417e-05, -2.439719008046828e-09, 3.409540996768416e-12, -11336.638638929715, -2.8137393273876885], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.778549117113386, -0.01850768009534956, 3.304251920801462e-05, -1.7651513955021242e-08, 3.166071810954609e-12, -16744.03557165474, -103.13108542290388], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[2.7297127369268974, 0.008710520141245999, -1.2913185211028592e-05, 1.0729500176894574e-08, -3.3943337365608772e-12, -31457.54854483086, -6.044789642349755], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[5.854969269446331, -0.003288483137573247, 5.569914269462162e-06, -2.7300850084335415e-09, 4.558987145762967e-13, -32149.48679199966, -21.35187313213533], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.30879122355327965, 0.02322708298302325, -3.556985631667207e-05, 2.7753574993128808e-08, -8.58545860359609e-12, 22898.39452832256, 2.811393303122383], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.1156067485700945, -0.00280518013919392, 5.1327085544999065e-06, -2.8290088062609482e-09, 5.200079218220455e-13, 21364.74158545415, -30.60961391779685], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.4742117971294497, 0.04214502799333202, -5.019760220276601e-05, 3.1922838335795355e-08, -8.249910061127297e-12, 10559.479151492667, 6.36470883708938], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.113329025757713, -0.009852176343404274, 1.7609574736677216e-05, -9.414962447585108e-09, 1.6903772966590764e-12, 6714.540908113755, -71.92239761319739], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.5193203736839918, 0.023734419820621105, -2.1291568139636634e-05, 9.945563692266576e-09, -1.7005351410229818e-12, -6268.490331548824, 7.353493090373176], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.145633263586134, -0.00875176973209202, 1.5480375529711203e-05, -8.15209374664918e-09, 1.4464145439879359e-12, -9052.639326184912, -46.97136392115422], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.0741220962649134, 0.02296559430760541, -1.226057329604347e-05, -1.2460185445705998e-09, 2.5403535857895596e-12, -39525.49807611515, 1.0295746326323805], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[13.048616847698872, -0.009848418313453733, 1.756721083280123e-05, -9.37554843041155e-09, 1.6816172124109935e-12, -42831.451480498494, -60.86265675446768], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.808924813123728, 0.05371463490268231, -6.677822116044849e-05, 4.327828231335019e-08, -1.1302340117674973e-11, 9619.113277671815, 17.849414393679496], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[14.066219490892804, -0.010480133424431765, 1.881923763885901e-05, -1.0130725757446001e-08, 1.8288331769112604e-12, 5034.884229558285, -76.61921501986114], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[3.3887757480036402, 0.014850717847752225, -1.805301669504195e-05, 1.2700305127677046e-08, -3.71603231477625e-12, -7392.432955153752, -8.571563660829092], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.154630679536853, -0.004498766040246608, 8.014670411137439e-06, -4.261301744603418e-09, 7.615164077904468e-13, -8827.883004523901, -37.55055639027854], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.37383224950975136, 0.023397710019633953, -1.9573586232432075e-05, 7.627211689445434e-09, -7.42111811754848e-13, -27513.515396526098, 6.579128815457124], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.314156069870133, -0.008568727985663858, 1.5185539446641045e-05, -8.02279709894677e-09, 1.4272209834821645e-12, -30326.02430156414, -47.989667356355966], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-4.541847849117079, 0.05160731365778216, -6.994895225460586e-05, 4.85158546002448e-08, -1.3456501060582005e-11, 17548.897787937152, 16.518060051423532], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.143026161240515, -0.007834157800508812, 1.4122649968247634e-05, -7.640524725824308e-09, 1.3848734905669914e-12, 13631.712020394687, -66.32284665500931], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.6073927476001146, 0.024113477843114503, -3.622640271683264e-05, 2.7097590534509488e-08, -7.934383325919752e-12, -4443.773913453174, -4.173471429435235], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.644642512159218, -0.002920107951806695, 5.169679573325273e-06, -2.71890373350085e-09, 4.823646822947716e-13, -5992.150911911304, -38.61488156962545], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.034362917556565, 0.02954891488791449, -3.738898950444786e-05, 2.505429465659623e-08, -6.773304924459906e-12, -421.82789016818003, 2.7569870106855787], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.38499077112822, -0.006270167025145126, 1.11635115950143e-05, -5.931883067828638e-09, 1.0600999248776385e-12, -2935.944194238502, -49.304152376772976], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.4078412812729548, 0.0338179878195214, -1.8236514452240962e-05, -2.1779846681167187e-10, 2.782370275839547e-12, -15394.262849522016, 3.0339923489881073], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.695291546486345, -0.016187385121103626, 2.891213543876439e-05, -1.5456084826553305e-08, 2.7742468574415523e-12, -20399.729563688914, -90.50551137177862], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.0434414251317503, 0.017236916874993947, -3.068697703256613e-05, 2.5388253643984168e-08, -8.015096471087081e-12, 8863.690938357384, 3.05464056120958], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.871023476836364, -0.00045958166167528366, 8.695001949282665e-07, -4.943271312311426e-10, 9.304071133495221e-14, 8127.66731954517, -15.466772477362655], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.04445744915912373, 0.019436774605162115, -1.9102879151143254e-05, 1.1126937588956332e-08, -2.7373593131227838e-12, -7912.647606732066, -0.17336363147096723], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.657044878275865, -0.007903077267106333, 1.4010043306489364e-05, -7.4001605167664224e-09, 1.315165879800811e-12, -10160.595329397735, -44.33525355508987], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.7634147945858656, 0.0219464658710969, -2.1033185174576587e-05, 1.0462359488040916e-08, -2.0084137966176905e-12, -1248.5787246803986, -2.2565254587769523], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.110542964967788, -0.006805475796930235, 1.209355201791198e-05, -6.412295380322582e-09, 1.1443173769024558e-12, -3673.8643094914296, -49.79892418653133], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.0757035196010083, 0.01735809071105879, -2.6092083573428506e-05, 1.892822722403096e-08, -5.388357485002043e-12, -4286.294101286677, 8.153626202260213], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[2.722479601930537, -0.0010681695731914382, 1.986535342963046e-06, -1.1204834620283936e-09, 2.0981144738444245e-13, -5338.342834452749, -15.32073643004469], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.9423313904266106, 0.024934892642416724, -2.791944843797565e-05, 1.5719586458373774e-08, -3.4902302905636923e-12, 881.6437935468562, -4.565885644842382], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.170220677721568, -0.004832588593152319, 8.689192774586976e-06, -4.6883153167852755e-09, 8.486222203068114e-13, -1431.1803385354597, -51.128805156393724], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.4822930278649229, 0.025871571199491405, -3.936039476990244e-05, 3.046297518767792e-08, -9.36533265787226e-12, -13050.060159087338, -3.573743737600349], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[8.070823546997097, -0.0030085226238067684, 5.515400196426425e-06, -3.048058667890981e-09, 5.614695355337743e-13, -14764.744063469028, -40.86261508054748], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.0278160088320707, 0.04868281219014872, -4.6469787174739195e-05, 2.2875187258704017e-08, -4.2387796327697976e-12, -9930.448111686654, 11.507104092070115], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[17.778763614366877, -0.015532208000049785, 2.7689844806460338e-05, -1.4757539182936681e-08, 2.6427553946709274e-12, -15317.520361930829, -94.26059354769245], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-2.755700439629306, 0.029312605794649855, -4.8437894188191764e-05, 3.8446911832162643e-08, -1.1723809146600604e-11, 1433.9644003054611, 10.096530030499576], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.828387360980449, -0.002459586682224992, 4.346754151488448e-06, -2.2753063265673523e-09, 4.0186534871427287e-13, -103.49030114074958, -26.36997010764379], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[4.177332163402245, -0.0012986540516224225, 2.5984622939912324e-06, -9.710016773295108e-10, -9.26337576537191e-14, 2010.884124583129, -7.8361294917540025], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[4.407824542775231, -0.0015051350963792515, 2.682566630104273e-06, -1.4261826867182169e-09, 2.544315810057889e-13, 1899.9796734994852, -9.198924896967895], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.6859727244306946, 0.025296488286088072, -3.43987529205198e-05, 2.4726477807501015e-08, -7.168138003378745e-12, 16296.596895665114, -8.130923604278514], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.122123145185716, -0.004680413340289875, 8.377743130666183e-06, -4.483216031568061e-09, 8.058109901272755e-13, 14297.698932103138, -50.07405524210492], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-3.1209931794395565, 0.039484923782041305, -5.467138983795234e-05, 3.872999629649474e-08, -1.0891104308381752e-11, 1883.1441621757554, 11.198444841797423], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.50734251320388, -0.006294471225312812, 1.1260009877515602e-05, -6.0234590216421404e-09, 1.0820106089978656e-12, -1038.8864192216406, -51.29677284416462], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.1400409666512144, 0.0358616573805749, -1.1102176671150235e-05, -8.973978217693699e-09, 5.916365065482844e-12, -17348.980106748335, -0.9771561017963037], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[21.506547199527056, -0.021538703607543497, 3.8413419358689606e-05, -2.0490479295625848e-08, 3.671042935515286e-12, -23472.396760004136, -113.46376258033209], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.5930119750582115, 0.0357123971055562, -2.8891957700799386e-05, 1.0354010548507836e-08, -6.877423743232263e-13, 7214.824803711391, 4.071149731697592], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.8597536839669, -0.012892247392929499, 2.298994138975832e-05, -1.226064568538439e-08, 2.1968936084718764e-12, 2847.1518923239273, -80.09977440115034], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.048539496567397, 0.028672134412854544, -3.4822727493620256e-05, 2.2596366150330564e-08, -5.960534505402434e-12, 5190.314199707034, 2.506598515261556], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[9.414354437146736, -0.006532482900153397, 1.1674953931296616e-05, -6.240267006137637e-09, 1.120140605442701e-12, 2623.525047805937, -49.970693413788126], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.38282616058402286, 0.031836927774111574, -4.013913643908383e-05, 2.76197059991355e-08, -7.788498432256708e-12, 14758.706032068718, 5.759691566008787], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.118041425372649, -0.007405977271224236, 1.326166656689412e-05, -7.105186320975667e-09, 1.277628341255651e-12, 11947.021025445954, -51.8345512580855], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.7048277092422881, 0.02837622327056927, -3.786454122395749e-05, 2.6544126539255356e-08, -7.541792545029187e-12, 37991.992621153906, -4.37179167652629], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[10.196865264094049, -0.00492541422276227, 8.881812446091055e-06, -4.805478550851786e-09, 8.71058813509183e-13, 35723.48692377084, -51.66534802230851], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.2361787460079208, 0.03911932656125317, -3.594457356435844e-05, 1.7078262888814518e-08, -3.0713100620497813e-12, -5050.419432818439, 3.5451000398087102], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[15.90734226084832, -0.01304854954877844, 2.331875870775683e-05, -1.2471530616531137e-08, 2.239506274355972e-12, -9539.161366308705, -83.81971063732256], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.0128370102000817, 0.03960548374689045, -2.417962420043452e-05, 3.235675321653288e-09, 1.9931520300565775e-12, -11692.46663115063, 3.3418589151508353], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[19.594121464710238, -0.018498151073632958, 3.295800995994865e-05, -1.7553531532329174e-08, 3.1414010692689637e-12, -17325.83384360716, -102.82847617515372], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[0.26316412282736656, 0.026729602411968388, -2.8237341091650866e-05, 1.616455490574562e-08, -3.698354050142505e-12, 9114.586327168887, -2.4462236547724867], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[11.199487227368975, -0.008342042432602436, 1.4711415811189053e-05, -7.709955049985035e-09, 1.3627207427774455e-12, 6354.245874314729, -57.701499632659676], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-1.2598047993537704, 0.042911094240943054, -6.112566082045491e-05, 4.4810530550478744e-08, -1.3045475719455122e-11, 23094.540296586787, 3.525331523354242], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.261893524177161, -0.006846928037540233, 1.224790567944862e-05, -6.547795140904026e-09, 1.175607426976468e-12, 19989.362405889035, -63.243841312769234], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[1.6007879331370871, 0.014704856571844503, -1.4669757091958005e-05, 6.819313569634828e-09, -1.147982283770417e-12, -12610.8227172237, -0.7662797899264149], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[7.295789997642349, -0.0025855481326240684, 4.764103709943176e-06, -2.6619174816996855e-09, 4.947906056262268e-13, -14096.822845174105, -29.782768933213145], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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
            NASAPolynomial(coeffs=[-0.6781966405200736, 0.03266565712193109, -3.482127801000223e-05, 1.920135282524885e-08, -4.230292086782209e-12, -18830.11603633195, 1.4808479870715603], Tmin=(298.0,'K'),Tmax=(1000.0, 'K')),
            NASAPolynomial(coeffs=[12.110968689306423, -0.007888924559054636, 1.4190152363739675e-05, -7.661288158980836e-09, 1.3863348748647986e-12, -22086.799129851534, -63.26465291869984], Tmin=(1000.0,'K'), Tmax=(2000.0, 'K')),
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

