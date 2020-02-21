#!/usr/bin/env python
# encoding: utf-8

name = "Surface Adsorption Corrections"
shortDesc = u""
longDesc = u"""
Changes due to adsorbing on a surface.
Here, Pt(111)
Note: "-h" means "horizontal".
"""

entry(
    index = 1,
    label = "R*",
    group=
"""
1 R  ux
2 X  ux
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   X
***********
This node should be empty, ensuring that one of the nodes below is used.


The group could well be defined as:

    1 R ux
    2 X ux

but then it is identical with the R*vdW node, and the database tests
do not like that. It should be OK, because things would check the
tree in order, and if there *was* a bond it would match either
R*bidentate or R*single_chemisorbed and thus not R*vdW.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 1,
#    label = "R-*",
#    group =
#"""
#1 X  u0 p0 c0 {2,S}
#2 R  u0 p0 c0 {1,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-2.46, -1.45, -0.78, -0.33, 0.18, 0.46, 0.74], 'cal/(mol*K)'),
#        H298=(-86.31, 'kcal/mol'),
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
# 1 X  u0 p0 c0
# 2 R  u0 p0 c0 {3,S}
# 3 R  u0 p0 c0 {2,S}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([0.92, 0.95, 0.97, 0.98, 0.98, 0.99, 0.99], 'cal/(mol*K)'),
#         H298=(-1.22, 'kcal/mol'),
#         S298=(-7.73, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from H2 vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 R  u0 p[0,1,2] c0 {2,S}
4 R  u0 p[0,1,2] c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.71, 1.22, 1.49, 1.65, 1.81, 1.9, 1.98], 'cal/(mol*K)'),
        H298=(6.47, 'kcal/mol'),
        S298=(-22.53, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2O vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.189 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18932 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 49.5 and 68.6 cm-1, where replaced by the 2D gas model.

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
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.09, 1.82, 2.2, 2.42, 2.65, 2.75, 2.86], 'cal/(mol*K)'),
        H298=(-34.86, 'kcal/mol'),
        S298=(-33.89, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.970 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.18039 eV, gamma_O(X) = 0.500.

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
    index = 5,
    label = "(OROR)*",
    group =
"""
1 X  u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.51, 1.74, 1.85, 1.92, 2.0, 2.05, 2.1], 'cal/(mol*K)'),
        H298=(15.92, 'kcal/mol'),
        S298=(-26.31, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HO-OH vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.286 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = -0.28574 eV, gamma_O(X) = 0.000.
            The two lowest frequencies, 10.6 and 50.4 cm-1, where replaced by the 2D gas model.

 RO-OR
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "O*O*",
    group =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.98, 2.83, 3.18, 3.31, 3.32, 3.26, 3.14], 'cal/(mol*K)'),
        H298=(14.04, 'kcal/mol'),
        S298=(-40.49, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from O2 bidentate, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.347 eV.
            Linear scaling parameters: ref_adatom_O1 = -3.586 eV, ref_adatom_O2 = -3.586 eV, psi = 3.23943 eV, gamma_O1(X) = 0.500, gamma_O2(X) = 0.500.

   O--O
   |  |
***** *****
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "O-*OR",
    group =
"""
1 X  u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.16, 4.53, 4.58, 4.53, 4.37, 4.24, 4.07], 'cal/(mol*K)'),
        H298=(5.63, 'kcal/mol'),
        S298=(-36.35, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from OOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.742 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 1.05105 eV, gamma_O(X) = 0.500.

   OR
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
1 X  u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.31, 0.21, 0.48, 0.63, 0.78, 0.86, 0.93], 'cal/(mol*K)'),
        H298=(-88.9, 'kcal/mol'),
        S298=(-30.95, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from O double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.030 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.00000 eV, gamma_O(X) = 1.000.

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
1 X  u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.24, 2.94, 3.33, 3.56, 3.78, 3.87, 3.95], 'cal/(mol*K)'),
        H298=(-24.64, 'kcal/mol'),
        S298=(-35.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from O-NH2 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.18, 2.44, 2.67, 2.86, 3.13, 3.3, 3.56], 'cal/(mol*K)'),
        H298=(-20.55, 'kcal/mol'),
        S298=(-40.61, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from O-CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.370 eV.
            Linear scaling parameters: ref_adatom_O = -3.586 eV, psi = 0.41957 eV, gamma_O(X) = 0.500.

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
1 X  u0 p0 c0
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
    shortDesc=u"""Came from NH3 vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,[S,D]}
3 R  u0 px c0 {2,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.86, 0.72, 1.69, 2.29, 2.94, 3.25, 3.59], 'cal/(mol*K)'),
        H298=(-48.33, 'kcal/mol'),
        S298=(-47.88, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NH2 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.74, -0.24, 0.7, 1.29, 1.93, 2.25, 2.6], 'cal/(mol*K)'),
        H298=(-80.92, 'kcal/mol'),
        S298=(-40.72, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NH double-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,T}
2 N  u0 p1 c0 {1,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.93, -0.2, 0.19, 0.42, 0.66, 0.78, 0.9], 'cal/(mol*K)'),
        H298=(-147.51, 'kcal/mol'),
        S298=(-32.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from N triple-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.36, 0.16, 0.59, 0.93, 1.37, 1.64, 1.92], 'cal/(mol*K)'),
        H298=(-4.37, 'kcal/mol'),
        S298=(-32.2, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2N-OH vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.22, 0.65, 1.14, 1.4, 1.61, 1.68, 1.77], 'cal/(mol*K)'),
        H298=(-18.76, 'kcal/mol'),
        S298=(-32.78, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-O vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.270 eV.
            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -1.26632 eV, gamma_N(X) = 0.000.
            The two lowest frequencies, 36.2 and 74.0 cm-1, where replaced by the 2D gas model.

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
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.82, 2.71, 3.18, 3.44, 3.72, 3.86, 3.98], 'cal/(mol*K)'),
        H298=(-21.0, 'kcal/mol'),
        S298=(-45.51, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-OH single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 O  u0 p2 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.48, 2.2, 2.6, 2.83, 3.02, 3.07, 3.06], 'cal/(mol*K)'),
        H298=(-25.86, 'kcal/mol'),
        S298=(-40.63, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NO single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,D} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.99, 2.43, 2.68, 2.82, 2.96, 3.00, 3.01], 'cal/(mol*K)'),
        H298=(-20.93, 'kcal/mol'),
        S298=(-35.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NO-h bidentate, double- and single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.16, 3.09, 3.5, 3.66, 3.71, 3.67, 3.65], 'cal/(mol*K)'),
        H298=(-64.4, 'kcal/mol'),
        S298=(-44.7, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from NOH double-bonded on Pt(111)""",
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
1 X  u0 p0 c0
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
        H298=(-23.19, 'kcal/mol'),
        S298=(-31.95, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2N-NH2 vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,D} {4,S}
3 N  u0 p1 c0 {2,D} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
        H298=(-20.58, 'kcal/mol'),
        S298=(-42.07, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-NH vdW-bonded on Pt(111)""",
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
#1 X  u0 p0 c0
#3 N  u0 p1 c0 {3,T}
#4 N  u0 p1 c0 {2,T}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
#        H298=(-2.39, 'kcal/mol'),
#        S298=(-15.27, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from NN vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.57, 2.38, 2.87, 3.19, 3.55, 3.73, 3.91], 'cal/(mol*K)'),
        H298=(-29.97, 'kcal/mol'),
        S298=(-45.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-NH2 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.42, 2.37, 2.9, 3.21, 3.47, 3.57, 3.69], 'cal/(mol*K)'),
        H298=(-25.14, 'kcal/mol'),
        S298=(-43.45, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from N-NH single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.71, 3.72, 4.13, 4.24, 4.1, 3.91, 3.71], 'cal/(mol*K)'),
        H298=(-47.66, 'kcal/mol'),
        S298=(-43.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from N-NH2 double-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.06, 3.29, 3.9, 4.17, 4.27, 4.22, 4.08], 'cal/(mol*K)'),
        H298=(-23.38, 'kcal/mol'),
        S298=(-42.53, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-NH-h bidentate, twice single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,S}
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
        H298=(-43.5, 'kcal/mol'),
        S298=(-46.63, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-CH3 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.62, 2.41, 2.85, 3.12, 3.4, 3.53, 3.7], 'cal/(mol*K)'),
        H298=(-39.08, 'kcal/mol'),
        S298=(-44.16, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from N-CH2 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.92, 1.54, 1.98, 2.29, 2.68, 2.93, 3.32], 'cal/(mol*K)'),
        H298=(-71.1, 'kcal/mol'),
        S298=(-47.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from N-CH3 double-bonded on Pt(111)""",
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
# 1 X  u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.92, 2.12, 2.17, 2.17, 2.13, 2.09, 2.04], 'cal/(mol*K)'),
#         H298=(-16.1, 'kcal/mol'),
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
1 X  u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.63, -0.71, -0.18, 0.14, 0.49, 0.67, 0.85], 'cal/(mol*K)'),
        H298=(-156.9, 'kcal/mol'),
        S298=(-31.82, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from C quadruple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.00000 eV, gamma_C(X) = 1.000.

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
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.8, 1.77, 2.28, 2.56, 2.8, 2.9, 2.96], 'cal/(mol*K)'),
        H298=(-137.32, 'kcal/mol'),
        S298=(-41.99, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from C-C bidentate, twice double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.910 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.84219 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.

  C--C
  |  |
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
1 X   u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.98, 0.54, 1.55, 2.21, 2.95, 3.32, 3.69], 'cal/(mol*K)'),
        H298=(-93.15, 'kcal/mol'),
        S298=(-48.06, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from C=CH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.60024 eV, gamma_C(X) = 0.500.

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
    index = 35,
    label = "C#*CR3",
    group =
"""
1 X  u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.8, 1.58, 2.11, 2.48, 2.93, 3.2, 3.53], 'cal/(mol*K)'),
        H298=(-129.74, 'kcal/mol'),
        S298=(-45.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from C-CH3 triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -5.590 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52567 eV, gamma_C(X) = 0.750.

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
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.92, -0.35, 0.62, 1.22, 1.87, 2.19, 2.56], 'cal/(mol*K)'),
        H298=(-145.5, 'kcal/mol'),
        S298=(-40.0, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -6.240 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.17590 eV, gamma_C(X) = 0.750.

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
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.04, 1.3, 2.2, 2.83, 3.57, 3.92, 4.17], 'cal/(mol*K)'),
        H298=(-47.33, 'kcal/mol'),
        S298=(-31.36, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH-CH bidentate, twice double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.010 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 4.74337 eV, gamma_C1(X) = 0.500, gamma_C2(X) = 0.500.

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
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.25, 0.39, 1.42, 2.06, 2.76, 3.1, 3.5], 'cal/(mol*K)'),
        H298=(-85.5, 'kcal/mol'),
        S298=(-42.7, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.640 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.26541 eV, gamma_C(X) = 0.500.

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
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
8 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.58, 2.74, 3.37, 3.72, 4.03, 4.14, 4.16], 'cal/(mol*K)'),
        H298=(-22.63, 'kcal/mol'),
        S298=(-41.46, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2-CH2 bidentate, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.950 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.42761 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.250.

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
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,[S,D]} {4,[S,D]}
3 R  u0 px c0 {2,[S,D]}
4 R  u0 px c0 {2,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.45, 0.61, 1.42, 2.02, 2.81, 3.26, 3.73], 'cal/(mol*K)'),
        H298=(-41.64, 'kcal/mol'),
        S298=(-32.73, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.770 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.08242 eV, gamma_C(X) = 0.250.

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
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
8 R  u0 p0 c0 {3,S}
9 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.01, 2.04, 2.05, 2.06, 2.07, 2.06, 2.05], 'cal/(mol*K)'),
        H298=(-4.65, 'kcal/mol'),
        S298=(-15.11, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3-CH3 vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.219 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.21852 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 5.6 and 8.8 cm-1, where replaced by the 2D gas model.

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
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.98, 2.0, 2.01, 2.01, 2.02, 2.02, 2.01], 'cal/(mol*K)'),
        H298=(-2.4, 'kcal/mol'),
        S298=(-6.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH4 vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.122 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.12206 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 3.2 and 8.1 cm-1, where replaced by the 2D gas model.

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
1 X  u0  p0 c0 {3,D}
2 X  u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,D} {4,D}
4 N  u0  p1 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.44, 2.71, 2.86, 2.96, 3.05, 3.07, 3.05], 'cal/(mol*K)'),
        H298=(-77.01, 'kcal/mol'),
        S298=(-34.98, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CN bidentate, double- and single-bonded on Pt(111)""",
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
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.15, 2.88, 3.33, 3.62, 3.93, 4.05, 4.11], 'cal/(mol*K)'),
        H298=(-40.56, 'kcal/mol'),
        S298=(-30.68, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CNH double-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S} {4,S} {5,S}
4 R  u0 p0 c0 {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.76, 3.37, 3.63, 3.74, 3.79, 3.77, 3.75], 'cal/(mol*K)'),
        H298=(-94.25, 'kcal/mol'),
        S298=(-49.82, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CNH2 triple-bonded on Pt(111)""",
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
# 1 X  u0  p0 c0 {2,D}
# 2 C  u0  p0 c0 {1,D} {3,D}
# 3 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.81, 2.37, 2.68, 2.88, 3.05, 3.1, 3.08], 'cal/(mol*K)'),
#         H298=(-23.38, 'kcal/mol'),
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
1 X  u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.82, 2.68, 3.13, 3.36, 3.54, 3.6, 3.67], 'cal/(mol*K)'),
        H298=(-87.68, 'kcal/mol'),
        S298=(-43.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from COH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.260 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.80370 eV, gamma_C(X) = 0.750.

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
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.26, 0.53, 1.67, 2.4, 3.19, 3.57, 3.9], 'cal/(mol*K)'),
        H298=(-65.6, 'kcal/mol'),
        S298=(-53.04, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-CH bidentate, single- and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.770 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 2.29437 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.

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
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {3,S}
8 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.61, 1.45, 2.08, 2.53, 3.11, 3.43, 3.77], 'cal/(mol*K)'),
        H298=(-40.97, 'kcal/mol'),
        S298=(-42.06, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-CH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.750 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.06163 eV, gamma_C(X) = 0.250.

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
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.5, 1.37, 1.81, 2.02, 2.14, 2.13, 2.08], 'cal/(mol*K)'),
        H298=(-5.98, 'kcal/mol'),
        S298=(-33.14, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-NH vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,S}
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
        H298=(-46.05, 'kcal/mol'),
        S298=(-39.03, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-NH2 single-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.91, 1.97, 2.0, 2.01, 2.02, 2.02, 2.01], 'cal/(mol*K)'),
        H298=(7.31, 'kcal/mol'),
        S298=(-20.91, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-O vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.184 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.18361 eV, gamma_C(X) = 0.000.

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
1 X  u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.84, 1.62, 2.2, 2.63, 3.19, 3.51, 3.84], 'cal/(mol*K)'),
        H298=(-44.61, 'kcal/mol'),
        S298=(-41.1, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2C-OH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.890 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.19820 eV, gamma_C(X) = 0.250.

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
1 X  u0 p0 c0
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
        H298=(-20.94, 'kcal/mol'),
        S298=(-33.73, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H3C-NH2 vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.38, 1.68, 1.82, 1.9, 1.96, 1.98, 2.0], 'cal/(mol*K)'),
        H298=(3.85, 'kcal/mol'),
        S298=(-28.83, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H3C-OH vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.316 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.31650 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 16.5 and 57.9 cm-1, where replaced by the 2D gas model.

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
1 X  u0  p0 c0 {3,S}
2 X  u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.7, 1.83, 2.54, 2.98, 3.47, 3.7, 3.9], 'cal/(mol*K)'),
        H298=(-95.45, 'kcal/mol'),
        S298=(-42.29, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HC-C bidentate, single- and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -4.100 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_C2 = -6.750 eV, psi = 0.96689 eV, gamma_C1(X) = 0.250, gamma_C2(X) = 0.500.

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
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
6 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.18, 1.6, 2.46, 2.99, 3.55, 3.79, 3.99], 'cal/(mol*K)'),
        H298=(-65.44, 'kcal/mol'),
        S298=(-48.91, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HC-CH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.790 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -1.09643 eV, gamma_C(X) = 0.250.

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
1 X  u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
6 R  u0 p0 c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.9, 1.71, 2.25, 2.61, 3.03, 3.26, 3.57], 'cal/(mol*K)'),
        H298=(-83.24, 'kcal/mol'),
        S298=(-44.11, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HC-CH3 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.580 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20205 eV, gamma_C(X) = 0.500.

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
1 X  u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.02, 0.68, 1.15, 1.46, 1.81, 1.96, 2.06], 'cal/(mol*K)'),
        H298=(-0.94, 'kcal/mol'),
        S298=(-22.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCN vdW-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.59, 1.77, 2.56, 3.08, 3.67, 3.93, 4.1], 'cal/(mol*K)'),
        H298=(-15.96, 'kcal/mol'),
        S298=(-35.76, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCN-h bidentate, twice double-bonded on Pt(111)""",
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
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.74, 2.48, 2.93, 3.22, 3.53, 3.67, 3.82], 'cal/(mol*K)'),
        H298=(-51.45, 'kcal/mol'),
        S298=(-38.15, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCNH single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.89, 2.02, 2.67, 3.07, 3.47, 3.65, 3.81], 'cal/(mol*K)'),
        H298=(-58.44, 'kcal/mol'),
        S298=(-46.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCNH-h bidentate, double- and single-bonded on Pt(111)""",
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
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.34, 3.12, 3.49, 3.66, 3.79, 3.81, 3.84], 'cal/(mol*K)'),
        H298=(-61.91, 'kcal/mol'),
        S298=(-37.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCNH2 double-bonded on Pt(111)""",
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
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.38, 2.19, 2.7, 3.02, 3.37, 3.53, 3.73], 'cal/(mol*K)'),
        H298=(-40.03, 'kcal/mol'),
        S298=(-36.89, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.210 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.52049 eV, gamma_C(X) = 0.250.

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
1 X  u0 p0 c0 {3,D}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.99, 2.22, 2.94, 3.34, 3.67, 3.78, 3.86], 'cal/(mol*K)'),
        H298=(-33.39, 'kcal/mol'),
        S298=(-45.92, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCO-h bidentate, double- and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -1.900 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.99512 eV, gamma_C1(X) = 0.500, gamma_O2(X) = 0.500.

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
1 X  u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.53, 2.45, 2.96, 3.26, 3.59, 3.75, 3.92], 'cal/(mol*K)'),
        H298=(-57.34, 'kcal/mol'),
        S298=(-39.75, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HCOH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -2.960 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 0.42191 eV, gamma_C(X) = 0.500.

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
1 X  u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=u'C-*R3',
    longDesc=u"""Thermo is currently for C-*R3.  Maybe should average all the children instead?""",
)

entry(
    index = 68,
    label = "N*",
    group =
"""
1 X  u0 {2,[S,D,T]}
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
1 X  u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=u'O-*R',
    longDesc=u"""Thermo is currently for O-*R.  Maybe should average all the children instead?""",
)

entry(
    index = 70,
    label = "R*single_chemisorbed",
    group =
"""
1 X  u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.07, 1.05, 1.77, 2.43, 2.8, 3.08, 3.39], 'cal/(mol*K)'),
        H298=(-41.61, 'kcal/mol'),
        S298=(-38.17, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Average of C-*R3, N-*R2 and O-*R thermo. """,
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "C*C*",
    group =
"""
1 X  u0 {3,[S,D]}
2 X  u0 {4,[S,D]}
3 C  u0 {1,[S,D]} {4,[S,D]}
4 C  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=u'C-*R2C-*R2',
    longDesc=u"""Thermo is currently for C-*R2C-*R2.  Maybe should average all the children instead?""",
)

entry(
    index = 72,
    label = "C*N*",
    group =
"""
1 X  u0 {3,[S,D]}
2 X  u0 {4,[S,D,T]}
3 C  u0 {1,[S,D]} {4,[S,D,T]}
4 N  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=u'C=*RN-*R',
    longDesc=u"""Thermo is currently for C=*RN-*R.  Maybe should average all the children instead?""",
)

entry(
    index = 73,
    label = "C*O*",
    group =
"""
1 X  u0 {3,[S,D,T]}
2 X  u0 {4,S}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 O  u0 {2,S} {3,[S,D,T]}
""",
    thermo=u'C=*RO-*',
)

entry(
    index = 74,
    label = "N*N*",
    group =
"""
1 X  u0 {3,[S,D]}
2 X  u0 {4,[S,D]}
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
1 X   u0 {3,[S,D,T]}
2 X   u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {4,[S,D,T]}
4 R!H ux {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.51, 2.68, 3.31, 3.65, 3.92, 4.00, 4.02], 'cal/(mol*K)'),
        H298=(-34.82, 'kcal/mol'),
        S298=(-43.39, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Average of C-*R2C-*R2, C=*RN-*R, C=*RO-* and N-*RN-*R thermo. """,
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "R*vdW",
    group =
"""
1 X  u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.23, 1.71, 2.00, 2.19, 2.39, 2.50, 2.61], 'cal/(mol*K)'),
        H298=(6.47, 'kcal/mol'),
        S298=(-22.53, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Average of (CR4)*, (NR3)* and (OR2)* thermo. """,
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "N*O*",
    group =
"""
1 X  u0 p0 c0 {3,[S,D]}
2 X  u0 p0 c0 {4,[S,D]}
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
#1 X  u0 p0 c0 {3,S}
#2 X  u0 p0 c0 {4,S}
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
#1 X  u0 c-1 {2,T}
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
1 X  u0 p0 {2,T}
2 N  u0 p1 {1,T}
""",
    thermo=u'N*',
)
entry(
    index = 80,
    label = "(CR3)*",
    group =
"""
1 X   u0
2 C   u0 {3,D} {4,S} {5,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
5 R   u0 {2,S}
""",
    thermo=u'(CR2NR)*',
    longDesc=u"""Perhaps should be an average?""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "(CR2)*",
    group =
"""
1 X   u0
2 C   u0 {3,T} {4,S}
3 R!H u0 {2,T}
4 R   u0 {2,S}
""",
    thermo=u'(CRN)*',
)

entry(
    index = 82,
    label = "(NR2CR3)*",
    group =
"""
1 X  u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 Cs u0 p0 c0 {2,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {2,S}
""",
    thermo=u'(NR3)*',
    longDesc=u"""Do we have data for this?""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 83,
    label = "(NR2)*",
    group =
"""
1 X   u0
2 N   u0 {3,D} {4,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
""",
    thermo=u'(NRO)*',
    longDesc=u"""Parent of (RN=O)* and (RN=NR)*. Should it be an average?""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 84,
    label = "N-*RN=*",
    group =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.83, 2.02, 2.69, 3.08, 3.41, 3.53, 3.66], 'cal/(mol*K)'),
        H298=(-30.55, 'kcal/mol'),
        S298=(-45.85, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from HN-N-h bidentate, single- and double-bonded on Pt(111)""",
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
    index = 85,
    label = "(CRCR)*",
    group =
"""
1 X  u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.02, 1.36, 1.56, 1.69, 1.82, 1.89, 1.95], 'cal/(mol*K)'),
        H298=(-4.70, 'kcal/mol'),
        S298=(-10.33, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from CH-CH vdW-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.200 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.20021 eV, gamma_C(X) = 0.000.
            The two lowest frequencies, 8.5 and 8.7 cm-1, where replaced by the 2D gas model.

  RC#CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "C-*R2N=*",
    group =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.01, 2.14, 2.79, 3.16, 3.5, 3.63, 3.76], 'cal/(mol*K)'),
        H298=(-40.44, 'kcal/mol'),
        S298=(-47.12, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2CN-h bidentate, single- and double-bonded on Pt(111)""",
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
    index = 87,
    label = "C-*R2N-*R",
    group =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.41, 3.0, 3.77, 4.11, 4.29, 4.28, 4.16], 'cal/(mol*K)'),
        H298=(-18.54, 'kcal/mol'),
        S298=(-47.43, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2CNH-h bidentate, twice single-bonded on Pt(111)""",
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
    index = 88,
    label = "C=*(=C)",
    group =
"""
1 X  u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.98, 0.54, 1.55, 2.21, 2.95, 3.32, 3.69], 'cal/(mol*K)'),
        H298=(-93.15, 'kcal/mol'),
        S298=(-48.06, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from C=CH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -3.980 eV.
            Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = -0.60024 eV, gamma_C(X) = 0.500.

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
    index = 89,
    label = "C-*R2O-*",
    group =
"""
1 X  u0 p0 c0 {3,S}
2 X  u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.02, 3.22, 3.83, 4.11, 4.25, 4.22, 4.11], 'cal/(mol*K)'),
        H298=(5.3, 'kcal/mol'),
        S298=(-41.48, 'cal/(mol*K)'),
    ),
    shortDesc=u"""Came from H2CO-h bidentate, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Jelena Jelic at KIT.
            DFT binding energy: -0.236 eV.
            Linear scaling parameters: ref_adatom_C1 = -6.750 eV, ref_adatom_O2 = -1.030 eV, psi = 1.96700 eV, gamma_C1(X) = 0.250, gamma_O2(X) = 0.500.

 R2C--O
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)




tree(
"""
L1: R*
    L2: R*bidentate
        L3: C*C*
            L4: C-*C-*
            L4: C=*RC=*R
            L4: C-*R2C-*R2
            L4: C-*R2C=*R
            L4: C-*RC=*
        L3: C*N*
            L4: C-*R2N=*
            L4: C-*R2N-*R
            L4: C=*N-*
            L4: C=*RN=*
            L4: C=*RN-*R
        L3: C*O*
            L4: C=*RO-*
            L4: C-*R2O-*
        L3: N*N*
            L4: N-*RN-*R
            L4: N-*RN=*
        L3: N*O*
            L4: N=*O-*
        L3: O*O*
    L2: R*single_chemisorbed
        L3: C*
            L4: Cq*
            L4: C#*R
                L5: C#*CR3
                L5: C#*NR2
                L5: C#*OR
            L4: C=*R2
                L5: C=*RCR3
                L5: C=*RNR2
                L5: C=*ROR
            L4: C=*(=R)
                L5: C=*(=C)
                L5: C=*(=NR)
            L4: C-*R3
                L5: C-*R2CR3
                L5: C-*R2NR2
                L5: C-*R2OR
                L5: C-*RCR2
                L5: C-*RNR
                L5: C-*RO
        L3: N*
            L4: N#*
            L4: N=*R
                L5: N=*CR3
                L5: N=*NR2
                L5: N=*OR
            L4: N-*R2
                L5: N-*RCR3
                L5: N-*RNR2
                L5: N-*ROR
                L5: N-*CR2
                L5: N-*NR
                L5: N-*O
        L3: O*
            L4: O=*
            L4: O-*R
                L5: O-*CR3
                L5: O-*NR2
                L5: O-*OR
    L2: R*vdW
        L3: (CR4)*
            L4: (CR3CR3)*
            L4: (CR3NR2)*
            L4: (CR3OR)*
        L3: (CR3)*
            L4: (CR2NR)*
            L4: (CR2O)*
        L3: (CR2)*
            L4: (CRN)*
            L4: (CRCR)*
        L3: (NR3)*
            L4: (NR2CR3)*
            L4: (NR2NR2)*
            L4: (NR2OR)*
        L3: (NR2)*
            L4: (NRO)*
            L4: (NRNR)*
        L3: (OR2)*
            L4: (OROR)*
""",
)
