#!/usr/bin/env python
# encoding: utf-8

name = "Adsorption Scaling"
shortDesc = u"Adsorption scaling (LSR)"
longDesc = u"""
Changes to the thermochemistry of adsorbtes from Pt(111) surface
"""

entry(
    index = 1,
    label = "R*",
    group=
"""
1 R  ux
2 * X ux
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   X
***********
This node should be empty, ensuring that one of the nodes below is used.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 1,
#    label = "R-*",
#    group =
#"""
#1 * X u0 p0 c0 {2,S}
#2 R  u0 p0 c0 {1,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-2.46, -1.45, -0.78, -0.33, 0.18, 0.46, 0.74], 'cal/(mol*K)'),
#        H298=(-58.54, 'kcal/mol'),
#        S298=(-26.39, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from H single-bonded on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -2.479 eV.
#            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.
#
#   R
#   |
#***********
#
#""",
#    metal = "Pt",
#    facet = "111",
#)

### This doesn't have a place in the tree, so I'm commenting it out. -- RHW
# entry(
#     index = 2,
#     label = "(R2)*",
#     group =
# """
# 1 * X u0 p0 c0
# 2 R  u0 p0 c0 {3,S}
# 3 R  u0 p0 c0 {2,S}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([0.92, 0.95, 0.97, 0.98, 0.98, 0.99, 0.99], 'cal/(mol*K)'),
#         H298=(-1.45, 'kcal/mol'),
#         S298=(-7.73, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from H2 physisorbed on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -0.054 eV.
#             Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
#             The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.
#
#   R-R
#    :
# ***********
#""",
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 3,
    label = "(OR2)*",
    group =
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.39, 8.41, 8.91, 9.16, 9.4, 9.51, 9.6], 'J/(mol*K)'),
        H298=(-49.08, 'kJ/mol'),
        S298=(-123.53, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2OX, HOOHX, CH3OHX, HCOOHX, CH3CH2OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.   
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method.    

 RO-R
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "O-*R",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0, 0, 0, 0, 0, 0, 0], 'J/(mol*K)'),
        H298=(0.5, 'kJ/mol'),
        S298=(0, 'J/(mol*K)'),
    ),
    shortDesc=u""" """,
    longDesc=u""" 

   R
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 8,
    label = "O=*",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0, 0, 0, 0, 0, 0, 0], 'J/(mol*K)'),
        H298=(1, 'kJ/mol'),
        S298=(0, 'J/(mol*K)'),
    ),
    shortDesc=u""" """,
    longDesc=u"""

   O
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "O-*NR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.24, 2.94, 3.33, 3.56, 3.78, 3.87, 3.95], 'cal/(mol*K)'),
        H298=(-30.61, 'kcal/mol'),
        S298=(-35.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XONH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.698 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.09537 eV, gamma_O(X) = 0.500.

   NR2
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "O-*CR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.44, 2.24, 2.93, 3.54, 4.49, 5.18, 6.35], 'J/(mol*K)'),
        H298=(-182.55, 'kJ/mol'),
        S298=(-149.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCH3, XOCH2CH3, and XOCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "(NR3)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.0, 1.92, 2.51, 2.9, 3.35, 3.59, 3.83], 'cal/(mol*K)'),
        H298=(-16.11, 'kcal/mol'),
        S298=(-32.0, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NH3X physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.673 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67337 eV, gamma_N(X) = 0.000.

 R2N-R
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "N-*R2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,[S,D]}
3 R  u0 px c0 {2,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.86, 0.72, 1.69, 2.29, 2.94, 3.25, 3.59], 'cal/(mol*K)'),
        H298=(-53.39, 'kcal/mol'),
        S298=(-47.88, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.030 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.58258 eV, gamma_N(X) = 0.333.

   NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 13,
    label = "N=*R",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.74, -0.24, 0.7, 1.29, 1.93, 2.25, 2.6], 'cal/(mol*K)'),
        H298=(-88.28, 'kcal/mol'),
        S298=(-40.72, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.440 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.54193 eV, gamma_N(X) = 0.667.

     NR
    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 14,
    label = "N#*",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.93, -0.2, 0.19, 0.42, 0.66, 0.78, 0.9], 'cal/(mol*K)'),
        H298=(-103.33, 'kcal/mol'),
        S298=(-32.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XN triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.352 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.

    N
   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 15,
    label = "(NR2OR)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.36, 0.16, 0.59, 0.93, 1.37, 1.64, 1.92], 'cal/(mol*K)'),
        H298=(-18.16, 'kcal/mol'),
        S298=(-32.2, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2XNOH physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.654 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.65407 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 17.1 and 68.9 cm-1, where replaced by the 2D gas model.

 R2N-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 16,
    label = "(NRO)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.74, 2.63, 3.12, 3.38, 3.6, 3.67, 3.76], 'cal/(mol*K)'),
        H298=(-39.84, 'kcal/mol'),
        S298=(-37.88, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HNOX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.

  RN=O
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 17,
    label = "N-*ROR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.82, 2.71, 3.18, 3.44, 3.72, 3.86, 3.98], 'cal/(mol*K)'),
        H298=(-44.41, 'kcal/mol'),
        S298=(-45.51, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HXNOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.08004 eV, gamma_N(X) = 0.333.

 R-N-OR
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "N-*O",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.48, 2.2, 2.6, 2.83, 3.02, 3.07, 3.06], 'cal/(mol*K)'),
        H298=(-47.5, 'kcal/mol'),
        S298=(-40.63, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.580 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.13417 eV, gamma_N(X) = 0.333.

   O
   ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "N=*O-*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.99, 2.43, 2.68, 2.82, 2.96, 3.00, 3.01], 'cal/(mol*K)'),
        H298=(-42.57, 'kcal/mol'),
        S298=(-35.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNXO bidentate, double- and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.390 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 1.51181 eV, gamma_N(X) = 0.667.

   N--O
  ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "N=*OR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.16, 3.09, 3.5, 3.66, 3.71, 3.67, 3.65], 'cal/(mol*K)'),
        H298=(-70.93, 'kcal/mol'),
        S298=(-44.7, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNOH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.260 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.35381 eV, gamma_N(X) = 0.667.

   OR
   |
   N
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 21,
    label = "(NR2NR2)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.1, 0.6, 0.94, 1.19, 1.5, 1.68, 1.88], 'cal/(mol*K)'),
        H298=(-26.81, 'kcal/mol'),
        S298=(-31.95, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NH2NH2X physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.977 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.97746 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 6.9 and 79.2 cm-1, where replaced by the 2D gas model.

 R2N-NR2
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "(NRNR)*",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
        H298=(-24.31, 'kcal/mol'),
        S298=(-42.07, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NHNHX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.676 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.67607 eV, gamma_N(X) = 0.000.

 RN=NR
   :
***********
""",
    metal = "Pt",
    facet = "111",
)


#entry(
#    index = 23,
#    label = "(NN)*",
#    group =
#"""
#1 * X u0 p0 c0
#3 N  u0 p1 c0 {3,T}
#4 N  u0 p1 c0 {2,T}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
#        H298=(-6.31, 'kcal/mol'),
#        S298=(-15.27, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from NN physisorbed on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.109 eV.
#            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.10949 eV, gamma_N(X) = 0.000.
#            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.
#
#  N#N
#   :
#***********
#"""
#)

entry(
    index = 24,
    label = "N-*RNR2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.57, 2.38, 2.87, 3.19, 3.55, 3.73, 3.91], 'cal/(mol*K)'),
        H298=(-40.74, 'kcal/mol'),
        S298=(-45.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHNH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.18029 eV, gamma_N(X) = 0.333.

 R-N-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "N-*NR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.42, 2.37, 2.9, 3.21, 3.47, 3.57, 3.69], 'cal/(mol*K)'),
        H298=(-37.65, 'kcal/mol'),
        S298=(-43.45, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNNH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.060 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.39360 eV, gamma_N(X) = 0.333.

   NR
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "N=*NR2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.71, 3.72, 4.13, 4.24, 4.1, 3.91, 3.71], 'cal/(mol*K)'),
        H298=(-59.44, 'kcal/mol'),
        S298=(-43.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNNH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.040 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.86160 eV, gamma_N(X) = 0.667.

   NR2
   |
   N
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "N-*RN-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.06, 3.29, 3.9, 4.17, 4.27, 4.22, 4.08], 'cal/(mol*K)'),
        H298=(-27.1, 'kcal/mol'),
        S298=(-42.53, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHXNH bidentate, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.982 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 1.91976 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.333.

 RN--NR
  |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 28,
    label = "N-*RCR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.96, 1.81, 2.36, 2.72, 3.14, 3.36, 3.63], 'cal/(mol*K)'),
        H298=(-51.48, 'kcal/mol'),
        S298=(-46.63, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.850 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.40192 eV, gamma_N(X) = 0.333.

 R-N-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "N-*CR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.62, 2.41, 2.85, 3.12, 3.4, 3.53, 3.7], 'cal/(mol*K)'),
        H298=(-50.13, 'kcal/mol'),
        S298=(-44.16, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.660 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.21342 eV, gamma_N(X) = 0.333.

   CR2
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "N=*CR3",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.92, 1.54, 1.98, 2.29, 2.68, 2.93, 3.32], 'cal/(mol*K)'),
        H298=(-84.35, 'kcal/mol'),
        S298=(-47.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH3 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.050 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.14794 eV, gamma_N(X) = 0.667.

   CR3
   |
   N
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

### Leads to AtomTypeError: Unable to determine atom type for atom O-, which has 3 single bonds, 0 double bonds to C, 0 double bonds to O, 0 double bonds to S, 0 triple bonds, 0 benzene bonds, 0 lone pairs, and 2 charge.
### And is not in the tree anyway, so commenting out. RHW
# entry(
#     index = 31,
#     label = "N-*O2",
#     group =
# """
# 1 * X u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.92, 2.12, 2.17, 2.17, 2.13, 2.09, 2.04], 'cal/(mol*K)'),
#         H298=(34.56, 'kcal/mol'),
#         S298=(-33.93, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from ON-O single-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#             The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.
#
#  O-N=O
#    |
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 32,
    label = "Cq*",
    group =
"""
1 * X u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.34, -3.34, -1.0, 0.42, 1.97, 2.73, 3.51], 'J/(mol*K)'),
        H298=(-657.91, 'kJ/mol'),
        S298=(-133.84, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XC quadruple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
 ||||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "C-*C-*",
    group =
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.31, 7.38, 9.53, 10.71, 11.76, 12.14, 12.4], 'J/(mol*K)'),
        H298=(-613.35, 'kJ/mol'),
        S298=(-163.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXC double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  C==C
 ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "C=*(=R)",
    group =
"""
1 * X  u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "C#*CR3",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.91, 1.58, 4.18, 6.07, 8.47, 9.86, 11.63], 'J/(mol*K)'),
        H298=(-594.9, 'kJ/mol'),
        S298=(-174.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH3, XCCH2CH3, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "C#*R",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.12, 2.73, 5.33, 7.1, 9.21, 10.37, 11.81], 'J/(mol*K)'),
        H298=(-571.12, 'kJ/mol'),
        S298=(-176.66, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH, XCCH3, XCOH, XCCHCH2, XCCH2CH3, XCCHO, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "C=*RC=*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.41, -0.06, 4.05, 6.96, 10.38, 12.03, 13.24], 'J/(mol*K)'),
        H298=(-221.27, 'kJ/mol'),
        S298=(-175.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C--C-R
  ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "C=*R2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.24, 3.87, 6.15, 7.64, 9.38, 10.32, 11.42], 'J/(mol*K)'),
        H298=(-370.06, 'kJ/mol'),
        S298=(-174.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2, CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3, XCHCHCH2, XCHCHO, XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "C-*R2C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
8 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.94, 10.72, 13.46, 15.04, 16.54, 17.1, 17.33], 'J/(mol*K)'),
        H298=(-124.09, 'kJ/mol'),
        S298=(-192.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2XCH2 and CH3XCHXCH2 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR2
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "C-*R3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.16, 2.29, 4.74, 6.49, 8.69, 9.93, 11.24], 'J/(mol*K)'),
        H298=(-212.02, 'kJ/mol'),
        S298=(-176.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, XCH2CHCH2, XCH2CHO, XCH3, CH3XCHCH3, CH3XCHOH, XCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "(CR3CR3)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.04, 9.93, 10.39, 10.67, 10.97, 11.11, 11.2], 'J/(mol*K)'),
        H298=(-29.6, 'kJ/mol'),
        S298=(-137.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3CH3X, CH3CH2CH3X, CH3CH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-CR3
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "(CR4)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.55, 9.48, 9.93, 10.16, 10.36, 10.44, 10.48], 'J/(mol*K)'),
        H298=(-41.27, 'kJ/mol'),
        S298=(-125.91, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH4X, CH3CH3X, CH3CH2CH3X, CH3CH2OHX, CH3OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R3C-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "C=*N-*",
    group =
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,D} {4,D}
4 N  u0  p1 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.44, 2.71, 2.86, 2.96, 3.05, 3.07, 3.05], 'cal/(mol*K)'),
        H298=(-88.23, 'kcal/mol'),
        S298=(-34.98, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXN bidentate, double- and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.340 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.13303 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.

  C==N
 ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "C=*(=NR)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.15, 2.88, 3.33, 3.62, 3.93, 4.05, 4.11], 'cal/(mol*K)'),
        H298=(-48.26, 'kcal/mol'),
        S298=(-30.68, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCNH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.740 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.63638 eV, gamma_C(X) = 0.500.

    NR
   ||
    C
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "C#*NR2",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.76, 3.37, 3.63, 3.74, 3.79, 3.77, 3.75], 'cal/(mol*K)'),
        H298=(-106.38, 'kcal/mol'),
        S298=(-49.82, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCNH2 triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.060 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.00119 eV, gamma_C(X) = 0.750.

   NR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)


## Not present in the tree
# entry(
#     index = 46,
#     label = "C=*O",
#     group =
# """
# 1 * X u0  p0 c0 {2,D}
# 2 C  u0  p0 c0 {1,D} {3,D}
# 3 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.81, 2.37, 2.68, 2.88, 3.05, 3.1, 3.08], 'cal/(mol*K)'),
#         H298=(-41.06, 'kcal/mol'),
#         S298=(-38.09, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from CO-f double-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -1.480 eV.
#             Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.
#
#    O
#   ||
#    C
#   ||
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 47,
    label = "C#*OR",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.83, 9.83, 11.9, 12.95, 13.69, 13.91, 14.43], 'J/(mol*K)'),
        H298=(-463.49, 'kJ/mol'),
        S298=(-187.54, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCOH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "C-*R2C=*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.74, 6.17, 9.66, 11.87, 14.28, 15.41, 16.39], 'J/(mol*K)'),
        H298=(-330.81, 'kJ/mol'),
        S298=(-214.97, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHXCH2, XCH2XCOH, XCHXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR
   |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "C-*R2CR3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.39, 3.93, 6.35, 8.02, 10.07, 11.2, 12.43], 'J/(mol*K)'),
        H298=(-214.46, 'kJ/mol'),
        S298=(-192.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, CH3XCHCH3, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
 R-C-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "(CR2NR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.5, 1.37, 1.81, 2.02, 2.14, 2.13, 2.08], 'cal/(mol*K)'),
        H298=(-12.55, 'kcal/mol'),
        S298=(-33.14, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2CNHX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.228 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.22807 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 46.0 and 79.7 cm-1, where replaced by the 2D gas model.

 R2C=NR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "C-*R2NR2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S} {6,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.1, 1.76, 2.28, 2.67, 3.19, 3.48, 3.79], 'cal/(mol*K)'),
        H298=(-53.29, 'kcal/mol'),
        S298=(-39.03, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2NH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.29283 eV, gamma_C(X) = 0.250.

   R
   |
 R-C-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "(CR2O)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.0, 6.87, 7.39, 7.72, 8.09, 8.27, 8.39], 'J/(mol*K)'),
        H298=(-73.08, 'kJ/mol'),
        S298=(-122.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2COX, HCOOHX, CH3CHOX, OCO2H2X, CH2COX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C=O
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "C-*R2OR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.14, 0.0, 2.2, 3.74, 5.64, 6.69, 7.8], 'J/(mol*K)'),
        H298=(-225.57, 'kJ/mol'),
        S298=(-157.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2OH, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

    R
    |
  R-C-OR
    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "(CR3NR2)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S} {7,S} {8,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
8 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.08, 0.64, 1.01, 1.25, 1.53, 1.68, 1.84], 'cal/(mol*K)'),
        H298=(-23.1, 'kcal/mol'),
        S298=(-33.73, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3NH2X physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.879 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.87925 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.6 and 84.5 cm-1, where replaced by the 2D gas model.

 R3C-NR2
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "(CR3OR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.44, 9.53, 10.02, 10.25, 10.41, 10.45, 10.47], 'J/(mol*K)'),
        H298=(-57.56, 'kJ/mol'),
        S298=(-139.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3OHX, CH3OCH3X, H2CO2H2X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "C-*RC=*",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.53, 3.23, 6.15, 7.98, 10.0, 10.99, 11.95], 'J/(mol*K)'),
        H298=(-440.52, 'kJ/mol'),
        S298=(-184.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXC single- and double bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 RC--C
  |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 57,
    label = "C-*RCR2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
6 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.29, 4.86, 7.35, 9.04, 10.97, 11.92, 12.82], 'J/(mol*K)'),
        H298=(-288.17, 'kJ/mol'),
        S298=(-182.51, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2XCCH3, CH2XCOH, XCHCCH2, XCHCH2, XCHCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "C=*RCR3",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.78, 4.72, 6.6, 7.86, 9.39, 10.26, 11.34], 'J/(mol*K)'),
        H298=(-372.23, 'kJ/mol'),
        S298=(-179.04, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "(CRN)*",
    group =
"""
1 * X u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.02, 0.68, 1.15, 1.46, 1.81, 1.96, 2.06], 'cal/(mol*K)'),
        H298=(-7.52, 'kcal/mol'),
        S298=(-22.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCNX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.010 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.00995 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 51.9 and 72.8 cm-1, where replaced by the 2D gas model.

 RC#N
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "C=*RN=*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.59, 1.77, 2.56, 3.08, 3.67, 3.93, 4.1], 'cal/(mol*K)'),
        H298=(-22.54, 'kcal/mol'),
        S298=(-35.76, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXNH, twice double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.650 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 2.37733 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.667.

  R
  |
  C--N
 ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 61,
    label = "C-*RNR",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.74, 2.48, 2.93, 3.22, 3.53, 3.67, 3.82], 'cal/(mol*K)'),
        H298=(-63.07, 'kcal/mol'),
        S298=(-38.15, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHNH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.220 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52691 eV, gamma_C(X) = 0.250.

   NR
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "C=*RN-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.89, 2.02, 2.67, 3.07, 3.47, 3.65, 3.81], 'cal/(mol*K)'),
        H298=(-70.06, 'kcal/mol'),
        S298=(-46.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXNH, double- and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.490 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.71054 eV, gamma_C1(X) = 0.500, gamma_N2(X) = 0.333.

 RC--NR
 ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 63,
    label = "C=*RNR2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.34, 3.12, 3.49, 3.66, 3.79, 3.81, 3.84], 'cal/(mol*K)'),
        H298=(-69.75, 'kcal/mol'),
        S298=(-37.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHNH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.670 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.70666 eV, gamma_C(X) = 0.500.

   NR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C-*RO",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.65, 2.4, 4.38, 5.69, 7.2, 7.95, 8.71], 'J/(mol*K)'),
        H298=(-282.27, 'kJ/mol'),
        S298=(-161.1, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged HXCO, OXCOH, CH3XCO, CHXCO, CH3CH2XCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C=O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "C=*RO-*",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.91, 10.27, 12.84, 14.27, 15.45, 15.81, 16.1], 'J/(mol*K)'),
        H298=(-238.17, 'kJ/mol'),
        S298=(-167.73, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R
  |
  C--O
 ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "C=*ROR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.05, 2.82, 4.47, 5.52, 6.78, 7.48, 8.24], 'J/(mol*K)'),
        H298=(-325.89, 'kJ/mol'),
        S298=(-146.57, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHOH and CH3XCOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "C*",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.31, 3.22, 5.55, 7.13, 8.99, 9.99, 11.1], 'J/(mol*K)'),
        H298=(-359.63, 'kJ/mol'),
        S298=(-173.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "N*",
    group =
"""
1 * X u0 {2,[S,D,T]}
2 N  ux {1,[S,D,T]}
""",
    thermo=u'N-*R2',
    longDesc=u"""Thermo is currently for N-*R2.  Maybe should average all the children instead?""",
)

entry(
    index = 69,
    label = "O*",
    group =
"""
1 * X u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.66, 7.38, 8.31, 8.88, 9.52, 9.88, 10.36], 'J/(mol*K)'),
        H298=(-215.12, 'kJ/mol'),
        S298=(-155.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "R*single-chemisorbed",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.84, 4.02, 6.08, 7.46, 9.09, 9.97, 10.96], 'J/(mol*K)'),
        H298=(-331.96, 'kJ/mol'),
        S298=(-169.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "C*C*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.88, 5.67, 8.7, 10.62, 12.69, 13.65, 14.5], 'J/(mol*K)'),
        H298=(-353.37, 'kJ/mol'),
        S298=(-192.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "C*N*",
    group =
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D]} {4,[S,D,T]}
4 N  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=u'C=*RN-*R',
    longDesc=u"""Thermo is currently for C=*RN-*R.  Maybe should average all the children instead?""",
)

#Changed the adjacency list because O can only have a single bond to the surface and another atom. 
#Always 2 free electron pairs. BK 2023/1/10
entry(
    index = 73,
    label = "C*O*",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {4,S}
4 O  u0 p2 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.34, 11.93, 14.46, 15.74, 16.6, 16.72, 16.63], 'J/(mol*K)'),
        H298=(-149.6, 'kJ/mol'),
        S298=(-169.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
    label = "N*N*",
    group =
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D]}
3 N  u0 {1,[S,D]} {4,[S,D]}
4 N  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=u'N-*RN-*R',
    longDesc=u"""Thermo is currently for N-*RN-*R.  Maybe should average all the children instead?""",
)

entry(
    index = 75,
    label = "R*bidentate",
    group =
"""
1 * X  u0 {3,[S,D,T]}
2 X  u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {4,[S,D,T]}
4 R!H ux {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.59, 6.37, 9.34, 11.19, 13.12, 13.99, 14.74], 'J/(mol*K)'),
        H298=(-330.73, 'kJ/mol'),
        S298=(-190.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "R*vdW",
    group =
"""
1 * X u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.25, 8.33, 8.9, 9.23, 9.56, 9.7, 9.8], 'J/(mol*K)'),
        H298=(-56.05, 'kJ/mol'),
        S298=(-125.18, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged of (CR4)*, (CR3)*, and (OR2)* (nitrogen is not included) on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "N*O*",
    group =
"""
1 * X u0 p0 c0 {3,[S,D]}
2 X u0 p0 c0 {4,[S,D]}
3 N  u0 p1 c0 {1,[S,D]} {4,[S,D]}
4 O  u0 p2 c0 {2,[S,D]} {3,[S,D]}
""",
    thermo=u'N=*O-*',
    longDesc=u"""Is there really any way to do N*O* besides N=*O-* ?""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 78,
#    label = "O*O*",
#    group =
#"""
#1 * X u0 p0 c0 {3,S}
#2 * X u0 p0 c0 {4,S}
#3 O  u0 p2 c0 {1,S} {4,S}
#4 O  u0 p2 c0 {2,S} {3,S}
#""",
#    thermo=u'O-*O-*',
#    longDesc=u"""Is there really any way to do O*O* besides O-*O-* ?""",
#    metal = "Pt",
#    facet = "111",
#)

###Have not been able to find any examples of when N is triple bonded to the surface and
###has an R group attached.  Redid for no R group below. --EM
#entry(
#    index = 79,
#    label = "N#*R",
#    group =
#"""
#1 * X u0 c-1 {2,T}
#2 N  u0 c+1 {1,T} {3,S}
#3 R  u0 c0  {2,S}
#""",
#    thermo=u'N*',
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 79,
    label = "N#*",
    group =
"""
1 * X u0 p0 {2,T}
2 N  u0 p1 {1,T}
""",
    thermo=u'N*',
    metal = "Pt",
    facet = "111",
)
entry(
    index = 80,
    label = "(CR3)*",
    group =
"""
1 * X  u0
2 C   u0 {3,D} {4,S} {5,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
5 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.68, 8.34, 8.74, 9.14, 9.32, 9.44], 'J/(mol*K)'),
        H298=(-74.45, 'kJ/mol'),
        S298=(-130.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "(CR2)*",
    group =
"""
1 * X  u0
2 C   u0 {3,T} {4,S}
3 R!H u0 {2,T}
4 R   u0 {2,S}
""",
    thermo=u'(CRCR)*',
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "(N=[O,N]R)*",
    group =
"""
1 * X    u0
2 N     u0 {3,D} {4,S}
3 [N,O] u0 {2,D}
4 R     u0 {2,S}
""",
    thermo=u'(NRO)*',
    longDesc=u"""Parent of (RN=O)* and (RN=NR)*. Should it be an average?""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "N-*RN=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.83, 2.02, 2.69, 3.08, 3.41, 3.53, 3.66], 'cal/(mol*K)'),
        H298=(-43.06, 'kcal/mol'),
        S298=(-45.85, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHXN single- and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.280 eV.
            Linear scaling parameters: ref_adatom_N1 = -4.352 eV, ref_adatom_N2 = -4.352 eV, psi = 3.07184 eV, gamma_N1(X) = 0.333, gamma_N2(X) = 0.667.

 RN--N
  |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "(CRCR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.69, 1.89, 2.02, 2.13, 2.46, 2.9, 3.96], 'J/(mol*K)'),
        H298=(-59.58, 'kJ/mol'),
        S298=(-115.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CHCHX and CHCCH3X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  RC#CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "C-*R2N=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.01, 2.14, 2.79, 3.16, 3.5, 3.63, 3.76], 'cal/(mol*K)'),
        H298=(-51.5, 'kcal/mol'),
        S298=(-47.12, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XN bidentate, single- and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.710 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = -0.37462 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.667.

 R2C--N
   |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "C-*R2N-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.41, 3.0, 3.77, 4.11, 4.29, 4.28, 4.16], 'cal/(mol*K)'),
        H298=(-25.1, 'kcal/mol'),
        S298=(-47.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XNH twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.756 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_N2 = 0.525 eV, psi = 0.75753 eV, gamma_C1(X) = 0.250, gamma_N2(X) = 0.333.

 R2C--NR
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 87,
    label = "C=*(=C)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "C-*R2O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.78, 13.6, 16.07, 17.2, 17.75, 17.62, 17.16], 'J/(mol*K)'),
        H298=(-61.03, 'kJ/mol'),
        S298=(-170.27, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--O
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "(CR2CR)*",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {2,D} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.43, 9.04, 9.92, 10.43, 10.9, 11.07, 11.17], 'J/(mol*K)'),
        H298=(-76.74, 'kJ/mol'),
        S298=(-143.86, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2CH2X, CH3CHCH2X, CH2CCH2X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C=CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 90,
    label = "C=*RC-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,D}
5 R  u0 px c0 {3,S}
6 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.37, 0.67, 4.68, 7.31, 10.25, 11.63, 12.69], 'J/(mol*K)'),
        H298=(-396.35, 'kJ/mol'),
        S298=(-202.17, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   RC---C=R
    ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "C#*C-*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.41, 8.3, 11.6, 13.47, 15.23, 15.91, 16.41], 'J/(mol*K)'),
        H298=(-440.28, 'kJ/mol'),
        S298=(-204.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH2 twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---C=R
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
    label = "C#*C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 R  u0 px c0 {4,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.9, 4.58, 8.22, 10.59, 13.24, 14.53, 15.76], 'J/(mol*K)'),
        H298=(-436.46, 'kJ/mol'),
        S298=(-201.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCXCH2 and XCXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---CR2
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 93,
    label = "C-*R2C-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,D}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.18, 10.54, 13.14, 14.74, 16.34, 16.95, 17.2], 'J/(mol*K)'),
        H298=(-179.99, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CXCH2 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  R2C--C=R
    |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "C-*RC-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.8, 1.82, 4.66, 6.68, 9.21, 10.78, 13.11], 'J/(mol*K)'),
        H298=(-227.58, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCCH3 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 RC==CR
  |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "C#*C=*R",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,D} {3,S} {5,S}
5 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.0, 1.29, 3.27, 4.54, 5.97, 6.69, 7.48], 'J/(mol*K)'),
        H298=(-488.53, 'kJ/mol'),
        S298=(-158.38, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH3 triple and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--CR
 ||| ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "C=*=R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,D} 
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.01, 2.84, 6.84, 9.5, 12.5, 13.99, 15.5], 'J/(mol*K)'),
        H298=(-543.25, 'kJ/mol'),
        S298=(-229.45, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHXCH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C=R--CR2
 ||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
    label = "R2C-*-R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.02, 3.61, 7.1, 9.67, 12.99, 14.82, 16.51], 'J/(mol*K)'),
        H298=(-389.14, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C--R--CR2
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "RC=*-R=C-*R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.06, -1.1, 2.74, 5.57, 9.12, 11.14, 13.63], 'J/(mol*K)'),
        H298=(-612.92, 'kJ/mol'),
        S298=(-200.99, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R==CR
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
    label = "RC-*=R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.12, 6.05, 9.54, 11.64, 13.78, 14.75, 15.73], 'J/(mol*K)'),
        H298=(-426.75, 'kJ/mol'),
        S298=(-227.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--CR2
  |      |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "RC=*-R-C-*R2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.57, -2.61, 1.61, 4.87, 9.19, 11.68, 14.45], 'J/(mol*K)'),
        H298=(-529.03, 'kJ/mol'),
        S298=(-222.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R--CR2
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "RC-*=R=C-*R",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.01, 7.65, 10.53, 12.32, 14.26, 15.17, 16.03], 'J/(mol*K)'),
        H298=(-370.79, 'kJ/mol'),
        S298=(-196.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==CR
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "RC-*=R=C=*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,D} {4,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.81, 3.88, 6.24, 7.94, 10.04, 11.14, 12.17], 'J/(mol*K)'),
        H298=(-432.93, 'kJ/mol'),
        S298=(-179.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==C
   |     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "O-*-C-O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 C  u0 p0 c0 {3,S} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.34, 8.03, 9.06, 10.2, 10.82, 11.57], 'J/(mol*K)'),
        H298=(-354.62, 'kJ/mol'),
        S298=(-179.72, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged OC(XO)XO and H2C(XO)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   O--R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "RC-*=R-O-*",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
6 R  u0 px c0 {3,S} 
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.77, 6.69, 9.4, 11.28, 13.55, 14.75, 15.95], 'J/(mol*K)'),
        H298=(-446.49, 'kJ/mol'),
        S298=(-211.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXO single and single -bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
    label = "C-*R2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 R!H u0  px c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.32, 3.63, 5.87, 7.37, 9.08, 9.94, 10.77], 'J/(mol*K)'),
        H298=(-285.22, 'kJ/mol'),
        S298=(-171.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "C=*RCR2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,D} {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.82, 4.08, 6.24, 7.7, 9.5, 10.49, 11.57], 'J/(mol*K)'),
        H298=(-379.17, 'kJ/mol'),
        S298=(-179.05, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHCHCH2 and XCHCHO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
    label = "C#*CR2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.45, 2.64, 4.89, 6.54, 8.67, 9.9, 11.29], 'J/(mol*K)'),
        H298=(-565.15, 'kJ/mol'),
        S298=(-180.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHCH2 and XCCHO triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)



tree(
"""
L1: R*
    L2: R*single-chemisorbed
        L3: C*
            L4: Cq*
            L4: C#*
            L4: C=*
            L4: C-*
        L3: N*
            L4: N#*
            L4: N=*
            L4: N-*
        L3: O*
            L4: O=*
            L4: O-*
        L3: H*
    L2: R*vdW
""",
)
