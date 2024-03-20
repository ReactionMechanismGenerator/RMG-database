#!/usr/bin/env python
# encoding: utf-8

name = "Solvent Descriptors"
shortDesc = u""
longDesc = u"""
Most of the Abraham (s_g, b_g, e_g, l_g, a_g, c_g) and Mintz solvent parameters (s_h, b_h, e_h, l_h, a_h, c_h) 
are fitted using experimental solute parameter, solvation free energy, and solvation enthalpy data.Abraham solvent parameters 
are used for solvation free energy (dGsolv) calculations, and Mintz solvent parameters are used for solvation enthalpy (dHsolv) calculations.
The fitting is described in:
    Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
    & Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.


The majority of the viscosity parameters (A, B, C, D, E) are obtained from:
    Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K., Rani, K. Y. (2007) Viscosity of Liquids.
    Springer, The Netherlands: Dordrecht.
The rest of the viscosity parameters are found from the DIPPR.

'alpha' and 'beta' are the SOLUTE parameters A and B that can be potentially used for intrinsic rate correction 
in H-abstraction rxns. But these parameters are currently not used in RMG.

'eps' is the dielectric constant of a solvent. It is currently not used in RMG.

'name_in_coolprop' represents the solvent's name used in the external package CoolProp. CoolProp is used for
fluid property calculation. If the solvent is not available in CoolProp, 'name_in_coolprop' is set to None.

'dataCount' stores the information on the number of data used to fit the Abraham and Mintz solvent parameters and 
their associated solvation free energy and solvation enthalpy mean absolute error (MAE).

Reference legend:
[Abraham2012] The hydrogen bond properties of water from 273 K to 573 K; equations for the prediction of gas-water partition coefficients Michael H. Abraham and William E. Acree Jr Phys. Chem. Chem. Phys., 2012,14, 7433–7440
[Abraham2016] Equations for the Partition of Neutral Molecules, Ionsand Ionic Species from Water to Water–MethanolMixtures Michael H. Abraham and William E. Acree Jr J Solution Chem (2016) 45:861–874
[Gagliardi2007] Static Dielectric Constants of Acetonitrile/Water Mixtures at Different Temperatures and Debye−Huckel A and a0B Parameters for Activity Coefficients Leonardo G. Gagliardi, Cecilia B. Castells, Clara Rafols, Marti Roses and, and Elisabeth Bosch, Journal of Chemical & Engineering Data 2007 52 (3), 1103-1107 DOI: 10.1021/je700055p
[JIRKAL2016] Application of Solvation Model to Prediction of the Solute Retention in Liquid Chromatography over a Wide Range of Mobile-Phase Compositions S. JIRKAL, M. MACHOVCOVA, AND J.G.K. SEVCIK DOI: 10.1556/1326.2016.28.1.06
[Mohsen-Nia2012] Measurement and modelling of static dielectric constants of aqueous solutions of methanol, ethanol and acetic acid at T = 293.15 K and 91.3 kPa M.Mohsen-Nia, H.Amiria https://doi.org/10.1016/j.jct.2012.08.009
"""

entry(
    index = 1,
    label = "water",
    molecule = "O",
    solvent = SolventData(
        # Abraham gas-to-solvent parameters for solvation free energy (dGsolv) correction at 298K
        s_g = 2.74983,
        b_g = 4.84491,
        e_g = 0.83346,
        l_g = -0.22544,
        a_g = 3.92725,
        c_g = -1.26188,
        # Mintz parameters for solvation enthaly (dHsolv) correction at 298K
        s_h = -0.75922,
        b_h = -28.45067,
        e_h = 10.57331,
        l_h = -5.87032,
        a_h = -26.34783,
        c_h = -11.63882,
        # viscosity parameters
        A = -52.843,
        B = 3703.6,
        C = 5.866,
        D = -5.88e-29,
        E = 10,
        # These are SOLUTE parameters that can be potentially used for intrinsic rate correction in H-abstraction rxns
        alpha = 0.353,
        beta = 0.38,
        # Dielectric constant
        eps = 80.4,
        # Name of the solvent used in the external fluid property calculation package, CoolProp.
        name_in_coolprop = "water",
    ),
    # The number of data used to fit the Abraham and Mintz parameters and their associated solvation free energy and
    # solvation enthalpy mean absolute error.
    dataCount = DataCountSolvent(
        dGsolvCount = 5224,
        dGsolvMAE = (0.17,'kcal/mol'),
        dHsolvCount = 58,
        dHsolvMAE = (1.04,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 2,
    label = "1-octanol",
    molecule = "CCCCCCCCO",
    solvent = SolventData(
        s_g = 0.71369,
        b_g = 1.42785,
        e_g = 0.01254,
        l_g = 0.85312,
        a_g = 3.52275,
        c_g = -0.18795,
        s_h = 4.37833,
        b_h = -9.58119,
        e_h = -0.21959,
        l_h = -9.17596,
        a_h = -53.32202,
        c_h = -5.69815,
        A = -0.022128,
        B = 3018.4,
        C = -2.8054,
        D = 1.3141e-05,
        E = 2,
        alpha = 0.328,
        beta = 0.45,
        eps = 10.3,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 4189,
        dGsolvMAE = (0.21,'kcal/mol'),
        dHsolvCount = 164,
        dHsolvMAE = (0.5,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
alpha = 0.328, #primary alcohols
beta = 0.45, #primary alcohols,
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 3,
    label = "benzene",
    molecule = "C1=CC=CC=C1",
    solvent = SolventData(
        s_g = 1.0749,
        b_g = 0.17492,
        e_g = -0.32585,
        l_g = 1.01356,
        a_g = 0.56683,
        c_g = 0.11597,
        s_h = -13.8578,
        b_h = -2.60662,
        e_h = 6.4422,
        l_h = -8.52047,
        a_h = -10.36551,
        c_h = -4.56882,
        A = 7.5117,
        B = 294.68,
        C = -2.794,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.14,
        eps = 2.3,
        name_in_coolprop = "benzene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 110,
        dGsolvMAE = (0.19,'kcal/mol'),
        dHsolvCount = 200,
        dHsolvMAE = (0.35,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 4,
    label = "cyclohexane",
    molecule = "C1CCCCC1",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.03443,
        e_g = -0.32662,
        l_g = 1.0347,
        a_g = 0.0,
        c_g = 0.24224,
        s_h = 1.62599,
        b_h = -1.42092,
        e_h = 2.5915,
        l_h = -9.03756,
        a_h = 2.25788,
        c_h = -6.74492,
        A = -33.763,
        B = 2497.2,
        C = 3.2236,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "CycloHexane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 122,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = 226,
        dHsolvMAE = (0.31,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 5,
    label = "dibutylether",
    molecule = "CCCCOCCCC",
    solvent = SolventData(
        s_g = 0.63588,
        b_g = -0.27257,
        e_g = -0.36266,
        l_g = 0.98243,
        a_g = 2.44885,
        c_g = 0.21775,
        s_h = -7.52607,
        b_h = 4.62445,
        e_h = 5.80308,
        l_h = -9.23463,
        a_h = -38.23245,
        c_h = -7.1917,
        A = 10.027,
        B = 206,
        C = -3.1607,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.45,
        eps = 3.1,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 90,
        dGsolvMAE = (0.2,'kcal/mol'),
        dHsolvCount = 78,
        dHsolvMAE = (0.27,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 6,
    label = "octane",
    molecule = "CCCCCCCC",
    solvent = SolventData(
        s_g = -0.03379,
        b_g = -0.15888,
        e_g = -0.14544,
        l_g = 1.00321,
        a_g = 0.01519,
        c_g = 0.21422,
        s_h = -0.97536,
        b_h = 0.96573,
        e_h = 2.83093,
        l_h = -9.21398,
        a_h = -2.37839,
        c_h = -6.58298,
        A = -98.805,
        B = 3905.5,
        C = 14.103,
        D = -2.5112e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "Octane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 185,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = 53,
        dHsolvMAE = (0.29,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 7,
    label = "butanol",
    molecule = "CCCCO",
    solvent = SolventData(
        s_g = 0.61135,
        b_g = 1.15917,
        e_g = -0.20375,
        l_g = 0.89029,
        a_g = 3.71643,
        c_g = 0.00297,
        s_h = 0.08507,
        b_h = -6.52791,
        e_h = 0.12537,
        l_h = -8.50864,
        a_h = -53.49993,
        c_h = -7.3014,
        A = -82.851,
        B = 4481.8,
        C = 11.182,
        D = -2.0943e-05,
        E = 2,
        alpha = 0.37,
        beta = 0.48,
        eps = 17.8,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 180,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = 133,
        dHsolvMAE = (0.47,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 8,
    label = "carbontet",
    molecule = "ClC(Cl)(Cl)Cl",
    solvent = SolventData(
        s_g = 0.4843,
        b_g = 0.23943,
        e_g = -0.32919,
        l_g = 1.03861,
        a_g = 0.11573,
        c_g = 0.2241,
        s_h = -5.25927,
        b_h = -6.24698,
        e_h = 3.73908,
        l_h = -8.92989,
        a_h = -0.85123,
        c_h = -6.17215,
        A = -8.0738,
        B = 1121.1,
        C = -0.4726,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.05,
        eps = 2.23,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 196,
        dGsolvMAE = (0.17,'kcal/mol'),
        dHsolvCount = 180,
        dHsolvMAE = (0.37,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
beta = 0.05, # Note 24 in Snelgrove et al. 2001
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 9,
    label = "chloroform",
    molecule = "ClC(Cl)Cl",
    solvent = SolventData(
        s_g = 1.10673,
        b_g = 1.35711,
        e_g = -0.60197,
        l_g = 1.00722,
        a_g = 0.39491,
        c_g = 0.18777,
        s_h = -13.13153,
        b_h = -17.63679,
        e_h = 8.58592,
        l_h = -8.57967,
        a_h = 0.85071,
        c_h = -7.4096,
        A = -14.109,
        B = 1049.2,
        C = 0.5377,
        D = 0,
        E = 0,
        alpha = 0.15,
        beta = 0.02,
        eps = 4.8,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 157,
        dGsolvMAE = (0.33,'kcal/mol'),
        dHsolvCount = 102,
        dHsolvMAE = (0.39,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 10,
    label = "decane",
    molecule = "CCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.08648,
        e_g = -0.10001,
        l_g = 0.99285,
        a_g = 0.10602,
        c_g = 0.16551,
        s_h = -2.28895,
        b_h = 4.22993,
        e_h = 2.52946,
        l_h = -9.16104,
        a_h = -4.30351,
        c_h = -6.80538,
        A = -97.662,
        B = 4342.7,
        C = 13.645,
        D = -1.9319e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "decane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 142,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = 48,
        dHsolvMAE = (0.35,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 11,
    label = "1,1-dichloroethane",
    molecule = "CC(Cl)Cl",
    solvent = SolventData(
        s_g = 1.436,
        b_g = 0.736,
        e_g = -0.15,
        l_g = 0.936,
        a_g = 0.649,
        c_g = 0.011,
        s_h = -18.328,
        b_h = -7.101,
        e_h = 5.555,
        l_h = -8.045,
        a_h = -9.599,
        c_h = -2.345,
        A = 15.312,
        B = -41.12,
        C = -3.919,
        D = 0,
        E = 0,
        alpha = 0.1,
        beta = 0.105,
        eps = 10.7,
        name_in_coolprop = None,
    ),
    dataCount = None,
    shortDesc = u""" """,
    longDesc = 
u"""
The source of the Abarham and Mintz parameters is unknown.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 12,
    label = "dimethylformamide",
    molecule = "N(C)(C)C=O",
    solvent = SolventData(
        s_g = 2.21609,
        b_g = -0.09698,
        e_g = -0.57987,
        l_g = 0.91023,
        a_g = 3.92841,
        c_g = -0.23856,
        s_h = -10.44289,
        b_h = -8.66852,
        e_h = -1.54729,
        l_h = -7.50889,
        a_h = -47.20336,
        c_h = -3.38497,
        A = -20.425,
        B = 1515.5,
        C = 1.4444,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.73,
        eps = 36.7,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 169,
        dGsolvMAE = (0.38,'kcal/mol'),
        dHsolvCount = 173,
        dHsolvMAE = (0.71,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 13,
    label = "dimethylsulfoxide",
    molecule = "CS(C)=O",
    solvent = SolventData(
        s_g = 2.63069,
        b_g = 0.04601,
        e_g = 0.1768,
        l_g = 0.67431,
        a_g = 5.5534,
        c_g = -0.43166,
        s_h = -19.09336,
        b_h = -4.51314,
        e_h = 0.32593,
        l_h = -6.36508,
        a_h = -47.86878,
        c_h = -2.59929,
        A = -37.347,
        B = 2835,
        C = 3.7937,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.88,
        eps = 46.7,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 63,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 157,
        dHsolvMAE = (0.53,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 14,
    label = "dodecane",
    molecule = "CCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 2e-05,
        b_g = -0.21632,
        e_g = -0.00463,
        l_g = 0.98261,
        a_g = 0.0,
        c_g = 0.11778,
        s_h = -2.32655,
        b_h = 1.7677,
        e_h = 2.17321,
        l_h = -9.25544,
        a_h = 5.82361,
        c_h = -6.24401,
        A = -134.91,
        B = 6054.2,
        C = 19.337,
        D = -2.443e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "Dodecane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 36,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = 35,
        dHsolvMAE = (0.3,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 15,
    label = "ethanol",
    molecule = "CCO",
    solvent = SolventData(
        s_g = 0.7177,
        b_g = 1.36437,
        e_g = -0.12249,
        l_g = 0.84352,
        a_g = 3.86403,
        c_g = 0.01722,
        s_h = 0.31824,
        b_h = -11.60122,
        e_h = -1.23158,
        l_h = -7.85082,
        a_h = -50.23362,
        c_h = -7.3821,
        A = 7.875,
        B = 781.98,
        C = -3.0418,
        D = 0,
        E = 0,
        alpha = 0.37,
        beta = 0.48,
        eps = 24.3,
        name_in_coolprop = "ethanol",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 231,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = 144,
        dHsolvMAE = (0.53,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 16,
    label = "heptane",
    molecule = "CCCCCCC",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.14762,
        e_g = -0.16189,
        l_g = 0.9899,
        a_g = 0.04796,
        c_g = 0.28069,
        s_h = -0.51333,
        b_h = 0.26048,
        e_h = 4.61586,
        l_h = -9.06675,
        a_h = 0.25492,
        c_h = -7.32177,
        A = -98.159,
        B = 3592.6,
        C = 14.197,
        D = -2.9555e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 1.9,
        name_in_coolprop = "Heptane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 218,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 162,
        dHsolvMAE = (0.34,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 17,
    label = "hexadecane",
    molecule = "CCCCCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.02644,
        e_g = 0.00864,
        l_g = 0.99636,
        a_g = 0.01678,
        c_g = 0.00648,
        s_h = -1.09109,
        b_h = -0.03074,
        e_h = 1.6109,
        l_h = -9.31861,
        a_h = -1.95026,
        c_h = -4.51577,
        A = -20.182,
        B = 2203.5,
        C = 1.2289,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0,
        eps = 2.08,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 260,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = 127,
        dHsolvMAE = (0.38,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 18,
    label = "hexane",
    molecule = "CCCCCC",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.13414,
        e_g = -0.24417,
        l_g = 0.9988,
        a_g = 0.0,
        c_g = 0.30308,
        s_h = 0.41891,
        b_h = 0.80271,
        e_h = 4.26513,
        l_h = -9.60641,
        a_h = 2.36579,
        c_h = -6.43283,
        A = -56.569,
        B = 2140.5,
        C = 7.5175,
        D = -1.7676e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "Hexane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 223,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 124,
        dHsolvMAE = (0.29,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 19,
    label = "isooctane",
    molecule = "CC(C)CC(C)(C)C",
    solvent = SolventData(
        s_g = 2e-05,
        b_g = -0.01222,
        e_g = -0.23538,
        l_g = 0.97967,
        a_g = 4e-05,
        c_g = 0.27445,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 0.0,
        l_h = -9.279,
        a_h = 0.0,
        c_h = 2.999,
        A = -12.928,
        B = 1137.5,
        C = 0.25725,
        D = -3.69e-28,
        E = 10,
        alpha = 0,
        beta = 0,
        eps = 1.94,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 163,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
The source of the Mintz parameters is unknown.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 20,
    label = "nonane",
    molecule = "CCCCCCCCC",
    solvent = SolventData(
        s_g = 0.04101,
        b_g = -0.21832,
        e_g = 0.01551,
        l_g = 0.9918,
        a_g = 0.0,
        c_g = 0.18699,
        s_h = 1.05931,
        b_h = -5.78133,
        e_h = 3.09976,
        l_h = -9.10555,
        a_h = 2.52293,
        c_h = -5.20391,
        A = -68.54,
        B = 3165.3,
        C = 9.0919,
        D = -1.3519e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "nonane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 69,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = 35,
        dHsolvMAE = (0.28,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 21,
    label = "pentane",
    molecule = "CCCCC",
    solvent = SolventData(
        s_g = 0.36197,
        b_g = -0.48912,
        e_g = -0.55148,
        l_g = 0.99415,
        a_g = -0.10836,
        c_g = 0.32869,
        s_h = -2.22875,
        b_h = -3.97897,
        e_h = 6.88359,
        l_h = -8.80102,
        a_h = -13.55874,
        c_h = -6.72014,
        A = -53.509,
        B = 1836.6,
        C = 7.1409,
        D = -1.9627e-05,
        E = 2,
        alpha = 0,
        beta = 0,
        eps = 1.8,
        name_in_coolprop = "Pentane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 51,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = 24,
        dHsolvMAE = (0.26,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 22,
    label = "toluene",
    molecule = "CC1C=CC=CC=1",
    solvent = SolventData(
        s_g = 0.90449,
        b_g = 0.11827,
        e_g = -0.31755,
        l_g = 1.03217,
        a_g = 0.58744,
        c_g = 0.08115,
        s_h = -13.6363,
        b_h = -3.5148,
        e_h = 6.20815,
        l_h = -8.36546,
        a_h = -8.10462,
        c_h = -5.65601,
        A = -226.08,
        B = 6805.7,
        C = 37.542,
        D = -0.060853,
        E = 1,
        alpha = 0,
        beta = 0.14,
        eps = 2.2,
        name_in_coolprop = "toluene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 77,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 111,
        dHsolvMAE = (0.36,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
eps = 2.2 # aerage of range 2.0-2.4
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 23,
    label = "undecane",
    molecule = "CCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.0,
        b_g = -0.13838,
        e_g = 0.03537,
        l_g = 0.96727,
        a_g = 0.05748,
        c_g = 0.13729,
        s_h = 0.0,
        b_h = 0.0,
        e_h = 2.999,
        l_h = -9.279,
        a_h = 0.0,
        c_h = -6.708,
        A = 52.176,
        B = -4951.9,
        C = -8.5676,
        D = 570980,
        E = -2,
        alpha = 0,
        beta = 0,
        eps = 2.0,
        name_in_coolprop = "Undecane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 24,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
The source of the Mintz parameters is unknown.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 24,
    label = "acetonitrile",
    molecule = "CC#N",
    solvent = SolventData(
        s_g = 2.485,
        b_g = 0.28401,
        e_g = -0.4984,
        l_g = 0.72236,
        a_g = 2.6609,
        c_g = 0.02099,
        s_h = -20.50487,
        b_h = -6.74961,
        e_h = 4.52844,
        l_h = -6.61759,
        a_h = -27.51588,
        c_h = -3.24474,
        A = -10.906,
        B = 872.02,
        C = 0,
        D = 0,
        E = 0,
        alpha = 0.04,
        beta = 0.33,
        eps = 37.5,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 70,
        dGsolvMAE = (0.1,'kcal/mol'),
        dHsolvCount = 81,
        dHsolvMAE = (0.51,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 25,
    label = "ethylacetate",
    molecule = "CCOC(C)=O",
    solvent = SolventData(
        s_g = 1.309,
        b_g = 0.09959,
        e_g = -0.33256,
        l_g = 0.90668,
        a_g = 2.85098,
        c_g = 0.21521,
        s_h = -14.52901,
        b_h = -2.30629,
        e_h = 4.39262,
        l_h = -7.7917,
        a_h = -29.06403,
        c_h = -6.06258,
        A = 14.354,
        B = -154.6,
        C = -3.7887,
        D = 0,
        E = 0,
        alpha = 0,
        beta = 0.45,
        eps = 6.0,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 134,
        dGsolvMAE = (0.25,'kcal/mol'),
        dHsolvCount = 82,
        dHsolvMAE = (0.4,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR
""",
)

entry(
    index = 26,
    label = "methanol",
    molecule = "CO",
    solvent = SolventData(
        s_g = 1.04295,
        b_g = 1.61785,
        e_g = -0.16578,
        l_g = 0.7628,
        a_g = 3.9997,
        c_g = 0.00565,
        s_h = -0.38202,
        b_h = -17.68008,
        e_h = -3.30961,
        l_h = -7.50486,
        a_h = -39.3694,
        c_h = -6.78364,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = 33.0,
        name_in_coolprop = "Methanol",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 173,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = 211,
        dHsolvMAE = (0.57,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
[Abraham2012]: Michael H. Abraham and William E. Acree Jr Phys. Chem. Chem. Phys., 2012,14, 7433–7440
[Mohsen-Nia2012]: DOI: 10.1016/j.jct.2012.08.009
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 27,
    label = "methanol_50_water_50",
    molecule = ["CO", "O"],
    solvent = SolventData(
        # Abraham gas-to-solvent (NOT water-to-solvent) parameters for free energy (G) correction at
        # parameter = gas-to-water + water-to-solvent = gas-to-solvent
        s_g = 2.521, # 2.743 + -0.222
        b_g = 3.067, # 4.814 + -1.747
        e_g = 1.045, # 0.822 + 0.223
        l_g = 1.449, # -0.213 + 1.662
        a_g = 4.168, # 3.904 + 0.264
        c_g = -1.248, # -1.271 + 0.023
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = 50.22,
        name_in_coolprop = None,
    ),
    dataCount = None,
    shortDesc = u""" """,
    longDesc = 
u"""
[Abraham2016]: Michael H. Abraham and William E. Acree Jr J Solution Chem (2016) 45:861–874
[Mohsen-Nia2012]: DOI: 10.1016/j.jct.2012.08.009
""",
)

entry(
    index = 28,
    label = "acetonitrile_40_water_60",
    molecule = ["CC#N", "O"],
    solvent = SolventData(
        # Abraham gas-to-solvent (NOT water-to-solvent) parameters for free energy (G) correction at
        # parameter = gas-to-water + water-to-solvent = gas-to-solvent
        s_g = 2.653, # 2.743 + -0.09
        b_g = 2.934, # 4.814 + -1.88
        e_g = 0.862, # 0.822 + 0.04
        l_g = 1.347, # -0.213 + 1.56
        a_g = 3.454, # 3.904 + -0.45
        c_g = -1.441, # -1.271 + -0.17
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = 60.61,
        name_in_coolprop = None,
    ),
    dataCount = None,
    shortDesc = u""" """,
    longDesc = 
u"""
[JIRKAL2016]: DOI: 10.1556/1326.2016.28.1.06
[Gagliardi2007]: DOI: 10.1021/je700055p
""",
)

entry(
    index = 29,
    label = "acetonitrile_60_water_40",
    molecule = ["CC#N", "O"],
    solvent = SolventData(
        # Abraham gas-to-solvent (NOT water-to-solvent) parameters for free energy (G) correction at
        # parameter = gas-to-water + water-to-solvent = gas-to-solvent
        s_g = 2.413, # 2.743 + -0.33
        b_g = 3.834, # 4.814 + -0.98
        e_g = 0.932, # 0.822 + 0.11
        l_g = 0.717, # -0.213 + 0.93
        a_g = 3.464, # 3.904 + -0.44
        c_g = -1.451, # -1.271 + -0.18
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = 51.05,
        name_in_coolprop = None,
    ),
    dataCount = None,
    shortDesc = u""" """,
    longDesc = 
u"""
[JIRKAL2016]: DOI: 10.1556/1326.2016.28.1.06
[Gagliardi2007]: DOI: 10.1021/je700055p
""",
)


entry(
    index = 30,
    label = "2-methylpyridine",
    molecule = "Cc1ccccn1",
    solvent = SolventData(
        s_g = 1.83487,
        b_g = -0.18942,
        e_g = -0.60952,
        l_g = 0.95433,
        a_g = 4.59331,
        c_g = 0.00409,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -23.569,
        B = 1733.2,
        C = 0,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 31,
    label = "4-methylpentan-2-one",
    molecule = "CC(=O)CC(C)C",
    solvent = SolventData(
        s_g = 0.88639,
        b_g = 0.5647,
        e_g = -0.13,
        l_g = 0.83639,
        a_g = 3.11628,
        c_g = 0.42248,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -33.781,
        B = 1955.3,
        C = 3.4673,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 24,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 32,
    label = "acetic acid",
    molecule = "CC(=O)O",
    solvent = SolventData(
        s_g = 1.85476,
        b_g = 1.27257,
        e_g = -0.73865,
        l_g = 0.77684,
        a_g = 1.75126,
        c_g = 0.04995,
        s_h = -2.41206,
        b_h = -24.31182,
        e_h = 2.05446,
        l_h = -8.87062,
        a_h = -33.36862,
        c_h = -1.5337,
        A = -9.03,
        B = 1212.3,
        C = -0.332,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = 92,
        dHsolvMAE = (0.41,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 33,
    label = "1-phenylethanone",
    molecule = "CC(=O)c1ccccc1",
    solvent = SolventData(
        s_g = 1.84302,
        b_g = 0.09327,
        e_g = -0.117,
        l_g = 0.84379,
        a_g = 2.97677,
        c_g = -0.0226,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 2.372,
        B = 807.0,
        C = -2.0158,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 24,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 34,
    label = "aniline",
    molecule = "Nc1ccccc1",
    solvent = SolventData(
        s_g = 2.20298,
        b_g = 0.96128,
        e_g = -0.30323,
        l_g = 0.77504,
        a_g = 2.78323,
        c_g = -0.2674,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -98.301,
        B = 6524.4,
        C = 1.8548,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 38,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 35,
    label = "anisole",
    molecule = "COc1ccccc1",
    solvent = SolventData(
        s_g = 1.7292,
        b_g = -0.02172,
        e_g = -0.49711,
        l_g = 0.92445,
        a_g = 1.61291,
        c_g = 0.03186,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -7.893,
        B = 1100.0,
        C = -0.477,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 36,
    label = "benzonitrile",
    molecule = "N#Cc1ccccc1",
    solvent = SolventData(
        s_g = 1.83958,
        b_g = 0.16621,
        e_g = -0.29361,
        l_g = 0.86898,
        a_g = 1.7869,
        c_g = -0.05162,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -20.236,
        B = 1737.4,
        C = 1.3531,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 57,
        dGsolvMAE = (0.1,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 37,
    label = "phenylmethanol",
    molecule = "OCc1ccccc1",
    solvent = SolventData(
        s_g = 1.49435,
        b_g = 1.27917,
        e_g = -0.25117,
        l_g = 0.82923,
        a_g = 3.87953,
        c_g = -0.26352,
        s_h = 204.97922,
        b_h = -500.02056,
        e_h = -71.66326,
        l_h = -5.01687,
        a_h = 390.86719,
        c_h = -15.17002,
        A = -14.859,
        B = 2865.7,
        C = 0,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 37,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = 8,
        dHsolvMAE = (0.06,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 38,
    label = "bromobenzene",
    molecule = "Brc1ccccc1",
    solvent = SolventData(
        s_g = 1.22545,
        b_g = 0.15934,
        e_g = -0.38545,
        l_g = 1.02925,
        a_g = 0.6297,
        c_g = -0.08273,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -12.307,
        B = 1173.4,
        C = 0.28397,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 76,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 39,
    label = "bromoethane",
    molecule = "CCBr",
    solvent = SolventData(
        s_g = 1.15717,
        b_g = 0.12059,
        e_g = -0.47702,
        l_g = 0.90841,
        a_g = 1.14817,
        c_g = 0.57026,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -8.3081,
        B = 764.58,
        C = -0.37699,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 40,
    label = "bromoform",
    molecule = "BrC(Br)Br",
    solvent = SolventData(
        s_g = -4.18454,
        b_g = -3.3668,
        e_g = 0.8598,
        l_g = 1.06256,
        a_g = 5.36705,
        c_g = 1.91762,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.586,
        B = 1295.5,
        C = 0.519,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 41,
    label = "butan-2-one",
    molecule = "CCC(C)=O",
    solvent = SolventData(
        s_g = 1.28552,
        b_g = 0.23586,
        e_g = -0.21354,
        l_g = 0.90855,
        a_g = 2.89388,
        c_g = 0.13707,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -8.134,
        B = 509.78,
        C = -1.5324,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 100,
        dGsolvMAE = (0.2,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 42,
    label = "butyl acetate",
    molecule = "CCCCOC(C)=O",
    solvent = SolventData(
        s_g = 1.34703,
        b_g = -0.24086,
        e_g = -0.47867,
        l_g = 0.94689,
        a_g = 2.68184,
        c_g = 0.17904,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -5.402,
        B = 688.0,
        C = -0.7296,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 97,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 43,
    label = "butylbenzene",
    molecule = "CCCCc1ccccc1",
    solvent = SolventData(
        s_g = 1.72279,
        b_g = -0.8784,
        e_g = -0.47146,
        l_g = 0.90944,
        a_g = 0.6158,
        c_g = 0.27038,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -25.102,
        B = 1949.6,
        C = 2.0385,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 44,
    label = "carbon disulfide",
    molecule = "S=C=S",
    solvent = SolventData(
        s_g = 0.40523,
        b_g = -0.12687,
        e_g = 0.17788,
        l_g = 1.01672,
        a_g = 0.11052,
        c_g = 0.24135,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -51.111,
        B = 2466.5,
        C = 6.1227,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 32,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 45,
    label = "chlorobenzene",
    molecule = "Clc1ccccc1",
    solvent = SolventData(
        s_g = 1.11261,
        b_g = 0.13081,
        e_g = -0.48771,
        l_g = 1.0438,
        a_g = 0.54146,
        c_g = 0.04732,
        s_h = -9.69601,
        b_h = -5.2003,
        e_h = 4.49706,
        l_h = -9.03846,
        a_h = -12.90418,
        c_h = -5.28551,
        A = -20.611,
        B = 1656.5,
        C = 1.4415,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 107,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = 127,
        dHsolvMAE = (0.31,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 46,
    label = "1-chlorohexane",
    molecule = "CCCCCCCl",
    solvent = SolventData(
        s_g = 1.06284,
        b_g = 1.12712,
        e_g = -2.26132,
        l_g = 0.8388,
        a_g = 0.07874,
        c_g = 0.21368,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 47,
    label = "cyclohexanone",
    molecule = "O=C1CCCCC1",
    solvent = SolventData(
        s_g = 1.55262,
        b_g = 0.00942,
        e_g = -0.25545,
        l_g = 0.91371,
        a_g = 2.7127,
        c_g = 0.03532,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 65,
        dGsolvMAE = (0.27,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 48,
    label = "decalin",
    molecule = "C1CCC2CCCCC2C1",
    solvent = SolventData(
        s_g = 0.44228,
        b_g = 0.81749,
        e_g = -0.10283,
        l_g = 0.96219,
        a_g = 0.18356,
        c_g = -0.34604,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 27,
        dGsolvMAE = (0.24,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 49,
    label = "decan-1-ol",
    molecule = "CCCCCCCCCCO",
    solvent = SolventData(
        s_g = 0.32457,
        b_g = 0.80963,
        e_g = -0.04793,
        l_g = 0.94427,
        a_g = 3.58108,
        c_g = -0.11436,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -80.656,
        B = 6325.5,
        C = 9.646,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 94,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 50,
    label = "1,1-dibromoethane",
    molecule = "CC(Br)Br",
    solvent = SolventData(
        s_g = -2.32449,
        b_g = -8.12457,
        e_g = -1.71075,
        l_g = 1.08506,
        a_g = 5.22341,
        c_g = 3.8382,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.1,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 51,
    label = "1,2-dichloroethane",
    molecule = "ClCCCl",
    solvent = SolventData(
        s_g = 1.82442,
        b_g = 0.34095,
        e_g = -0.50577,
        l_g = 0.92031,
        a_g = 0.82692,
        c_g = 0.06113,
        s_h = -18.66947,
        b_h = -6.67126,
        e_h = 5.89296,
        l_h = -8.06112,
        a_h = -9.78992,
        c_h = -2.39299,
        A = 8.875,
        B = 264.0,
        C = -2.9714,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "Dichloroethane",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 115,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 92,
        dHsolvMAE = (0.34,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 52,
    label = "ethoxyethane",
    molecule = "CCOCC",
    solvent = SolventData(
        s_g = 0.70667,
        b_g = -0.32535,
        e_g = -0.27937,
        l_g = 0.96121,
        a_g = 3.31215,
        c_g = 0.36129,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 10.197,
        B = -63.8,
        C = -3.226,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "DiethylEther",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 143,
        dGsolvMAE = (0.31,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 53,
    label = "2-propan-2-yloxypropane",
    molecule = "CC(C)OC(C)C",
    solvent = SolventData(
        s_g = 0.65056,
        b_g = -0.28503,
        e_g = -0.34893,
        l_g = 0.94504,
        a_g = 2.94474,
        c_g = 0.39615,
        s_h = -8.31857,
        b_h = 0.05378,
        e_h = 6.2166,
        l_h = -6.28874,
        a_h = -0.0,
        c_h = -13.29248,
        A = -11.5,
        B = 993.0,
        C = 0.29272,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 63,
        dGsolvMAE = (0.2,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.1,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 54,
    label = "N,N-dimethylacetamide",
    molecule = "CC(=O)N(C)C",
    solvent = SolventData(
        s_g = 1.91518,
        b_g = -0.35012,
        e_g = -0.79736,
        l_g = 1.03469,
        a_g = 4.85283,
        c_g = -0.26318,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 22.738,
        B = -428.5,
        C = -4.967,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 101,
        dGsolvMAE = (0.34,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 55,
    label = "ethoxybenzene",
    molecule = "CCOc1ccccc1",
    solvent = SolventData(
        s_g = 1.56905,
        b_g = -0.3437,
        e_g = -0.22907,
        l_g = 0.93061,
        a_g = 1.60257,
        c_g = 0.07477,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -55.996,
        B = 3521.6,
        C = 6.5648,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 56,
    label = "ethylbenzene",
    molecule = "CCc1ccccc1",
    solvent = SolventData(
        s_g = 0.99102,
        b_g = -0.24581,
        e_g = -0.24576,
        l_g = 1.00485,
        a_g = 0.26071,
        c_g = 0.20989,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -10.452,
        B = 1048.4,
        C = -0.0715,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "EthylBenzene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 33,
        dGsolvMAE = (0.18,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 57,
    label = "fluorobenzene",
    molecule = "Fc1ccccc1",
    solvent = SolventData(
        s_g = 1.16035,
        b_g = 0.4474,
        e_g = -0.51966,
        l_g = 0.97958,
        a_g = 0.63162,
        c_g = 0.17985,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -10.064,
        B = 1058.7,
        C = -0.17162,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 30,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 58,
    label = "heptan-1-ol",
    molecule = "CCCCCCCO",
    solvent = SolventData(
        s_g = 0.53076,
        b_g = 0.81028,
        e_g = -0.23386,
        l_g = 0.93819,
        a_g = 3.62031,
        c_g = -0.04861,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -88.623,
        B = 6463.8,
        C = 10.846,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 83,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 59,
    label = "1-iodohexadecane",
    molecule = "CCCCCCCCCCCCCCCCI",
    solvent = SolventData(
        s_g = 1.19885,
        b_g = -3.01135,
        e_g = 0.07743,
        l_g = 0.9049,
        a_g = -1.26212,
        c_g = -0.027,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 60,
    label = "hexan-1-ol",
    molecule = "CCCCCCO",
    solvent = SolventData(
        s_g = 0.53349,
        b_g = 0.90075,
        e_g = -0.20991,
        l_g = 0.92234,
        a_g = 3.68129,
        c_g = -0.02862,
        s_h = 2.04603,
        b_h = -11.44571,
        e_h = -0.525,
        l_h = -9.21845,
        a_h = -45.73846,
        c_h = -4.98156,
        A = -38.503,
        B = 3810.4,
        C = -0.89719,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 107,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 85,
        dHsolvMAE = (0.44,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 61,
    label = "iodobenzene",
    molecule = "Ic1ccccc1",
    solvent = SolventData(
        s_g = 1.29387,
        b_g = 0.33603,
        e_g = -0.21232,
        l_g = 1.0175,
        a_g = 0.31999,
        c_g = -0.25948,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 0.25,
        B = 535.2,
        C = -1.6207,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 39,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 62,
    label = "2-methylpropan-1-ol",
    molecule = "CC(C)CO",
    solvent = SolventData(
        s_g = 0.53584,
        b_g = 1.44702,
        e_g = -0.26984,
        l_g = 0.87559,
        a_g = 3.63592,
        c_g = 0.01174,
        s_h = 1.9962,
        b_h = -8.70067,
        e_h = 4.63079,
        l_h = -8.61458,
        a_h = -53.97057,
        c_h = -7.13202,
        A = -48.035,
        B = 4306.7,
        C = 4.8948,
        D = -3.5e-28,
        E = 10,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 120,
        dGsolvMAE = (0.19,'kcal/mol'),
        dHsolvCount = 98,
        dHsolvMAE = (0.41,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 63,
    label = "propan-2-ol",
    molecule = "CC(C)O",
    solvent = SolventData(
        s_g = 0.65341,
        b_g = 1.14881,
        e_g = -0.31864,
        l_g = 0.88495,
        a_g = 4.0022,
        c_g = -0.02455,
        s_h = 3.84923,
        b_h = -8.74711,
        e_h = -1.46393,
        l_h = -8.00127,
        a_h = -48.6278,
        c_h = -7.79417,
        A = -8.23,
        B = 2282.2,
        C = -0.98495,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 157,
        dGsolvMAE = (0.19,'kcal/mol'),
        dHsolvCount = 112,
        dHsolvMAE = (0.48,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 64,
    label = "cumene",
    molecule = "CC(C)c1ccccc1",
    solvent = SolventData(
        s_g = 0.08762,
        b_g = -0.06313,
        e_g = -0.54482,
        l_g = 0.95983,
        a_g = 0.0185,
        c_g = 0.82117,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -24.438,
        B = 1785.9,
        C = 1.972,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 65,
    label = "3-methylphenol",
    molecule = "Cc1cccc(O)c1",
    solvent = SolventData(
        s_g = 0.82561,
        b_g = 3.62143,
        e_g = -0.45065,
        l_g = 0.78463,
        a_g = 2.02685,
        c_g = 0.08479,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -124.95,
        B = 8727.8,
        C = 16.012,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 14,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 66,
    label = "2-methoxyethanol",
    molecule = "COCCO",
    solvent = SolventData(
        s_g = 2.34242,
        b_g = -0.1546,
        e_g = -0.57619,
        l_g = 0.76933,
        a_g = 4.54298,
        c_g = -0.07992,
        s_h = -30.69328,
        b_h = 0.11722,
        e_h = 12.75437,
        l_h = -8.84607,
        a_h = -37.86032,
        c_h = 1.58484,
        A = -3.4217,
        B = 1792.6,
        C = -1.5878,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 39,
        dGsolvMAE = (0.2,'kcal/mol'),
        dHsolvCount = 23,
        dHsolvMAE = (0.3,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 67,
    label = "dichloromethane",
    molecule = "ClCCl",
    solvent = SolventData(
        s_g = 1.71687,
        b_g = 0.57955,
        e_g = -0.69144,
        l_g = 0.96665,
        a_g = 0.35236,
        c_g = 0.18753,
        s_h = -14.36353,
        b_h = -10.79672,
        e_h = 4.7822,
        l_h = -7.75762,
        a_h = -2.39211,
        c_h = -5.36242,
        A = -13.071,
        B = 940.03,
        C = 0.3733,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 58,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 108,
        dHsolvMAE = (0.4,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 68,
    label = "N-methylformamide",
    molecule = "CNC=O",
    solvent = SolventData(
        s_g = 1.89971,
        b_g = 0.63051,
        e_g = -0.194,
        l_g = 0.71737,
        a_g = 4.03684,
        c_g = -0.18927,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 9.9223,
        B = 466.32,
        C = -3.1375,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 54,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 69,
    label = "nitrobenzene",
    molecule = "O=[N+]([O-])c1ccccc1",
    solvent = SolventData(
        s_g = 1.84995,
        b_g = 0.28563,
        e_g = -0.22978,
        l_g = 0.89259,
        a_g = 1.35539,
        c_g = -0.18912,
        s_h = -46.29472,
        b_h = 44.50457,
        e_h = 27.13188,
        l_h = -6.47435,
        a_h = -0.0,
        c_h = -9.65935,
        A = -34.557,
        B = 2611.3,
        C = 3.4283,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 54,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.27,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 70,
    label = "1-nitroethane",
    molecule = "CC[N+](=O)[O-]",
    solvent = SolventData(
        s_g = 2.2979,
        b_g = -0.04923,
        e_g = -0.57792,
        l_g = 0.64296,
        a_g = 1.66858,
        c_g = 0.51669,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -4.438,
        B = 746.5,
        C = -0.9385,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 71,
    label = "nitromethane",
    molecule = "C[N+](=O)[O-]",
    solvent = SolventData(
        s_g = 1.76232,
        b_g = 1.1804,
        e_g = 0.27851,
        l_g = 0.62995,
        a_g = 1.80611,
        c_g = 0.00448,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -17.684,
        B = 1358.0,
        C = 1.011,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.19,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 72,
    label = "nonan-1-ol",
    molecule = "CCCCCCCCCO",
    solvent = SolventData(
        s_g = 0.4669,
        b_g = 1.33538,
        e_g = -0.06234,
        l_g = 0.88487,
        a_g = 3.8611,
        c_g = -0.15305,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -7.1348,
        B = 2776.3,
        C = -1.2064,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 28,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 73,
    label = "1,2-dichlorobenzene",
    molecule = "Clc1ccccc1Cl",
    solvent = SolventData(
        s_g = 0.90799,
        b_g = 0.86727,
        e_g = 0.12499,
        l_g = 1.12073,
        a_g = 0.42881,
        c_g = -0.85004,
        s_h = -9.81485,
        b_h = -5.48747,
        e_h = 4.46035,
        l_h = -9.14429,
        a_h = -8.69333,
        c_h = -4.66197,
        A = -22.216,
        B = 1758.2,
        C = 1.7011,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = 91,
        dHsolvMAE = (0.31,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 74,
    label = "pentadecane",
    molecule = "CCCCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.24876,
        b_g = -0.32594,
        e_g = 0.06094,
        l_g = 0.98868,
        a_g = 0.9794,
        c_g = 0.07093,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -19.299,
        B = 2088.6,
        C = 1.1091,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 20,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 75,
    label = "pentan-1-ol",
    molecule = "CCCCCO",
    solvent = SolventData(
        s_g = 0.55018,
        b_g = 1.04699,
        e_g = -0.21225,
        l_g = 0.90653,
        a_g = 3.74136,
        c_g = -0.00817,
        s_h = 1.94124,
        b_h = -9.01807,
        e_h = 3.97932,
        l_h = -9.16523,
        a_h = -53.07544,
        c_h = -6.22045,
        A = -22.758,
        B = 2916.9,
        C = 1.2839,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 146,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 92,
        dHsolvMAE = (0.46,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 76,
    label = "hexafluorobenzene",
    molecule = "Fc1c(F)c(F)c(F)c(F)c1F",
    solvent = SolventData(
        s_g = 1.18649,
        b_g = -0.03657,
        e_g = -0.3372,
        l_g = 0.8015,
        a_g = -0.79769,
        c_g = 0.74792,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.687,
        B = 1916.0,
        C = 0.24197,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 20,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 77,
    label = "propan-1-ol",
    molecule = "CCCO",
    solvent = SolventData(
        s_g = 0.79125,
        b_g = 1.13116,
        e_g = -0.2722,
        l_g = 0.86906,
        a_g = 3.82092,
        c_g = -0.01635,
        s_h = 5.86728,
        b_h = -9.40849,
        e_h = -3.32505,
        l_h = -8.10341,
        a_h = -50.00797,
        c_h = -8.6506,
        A = 0.571,
        B = 1521.0,
        C = -2.0894,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 164,
        dGsolvMAE = (0.22,'kcal/mol'),
        dHsolvCount = 119,
        dHsolvMAE = (0.55,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 78,
    label = "pyridine",
    molecule = "c1ccncc1",
    solvent = SolventData(
        s_g = 2.38048,
        b_g = -0.64239,
        e_g = -0.55343,
        l_g = 0.893,
        a_g = 4.9189,
        c_g = 0.00782,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -51.584,
        B = 3135.5,
        C = 5.9733,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 19,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 79,
    label = "butan-2-ol",
    molecule = "CCC(C)O",
    solvent = SolventData(
        s_g = 0.6972,
        b_g = 0.9333,
        e_g = -0.38628,
        l_g = 0.90951,
        a_g = 3.8415,
        c_g = -0.0095,
        s_h = 3.62815,
        b_h = -9.24459,
        e_h = 1.5237,
        l_h = -8.34576,
        a_h = -50.69463,
        c_h = -6.74398,
        A = -106.38,
        B = 7434.0,
        C = 13.285,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 110,
        dGsolvMAE = (0.18,'kcal/mol'),
        dHsolvCount = 89,
        dHsolvMAE = (0.46,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 80,
    label = "tert-butylbenzene",
    molecule = "CC(C)(C)c1ccccc1",
    solvent = SolventData(
        s_g = 0.88156,
        b_g = -0.54391,
        e_g = -0.62169,
        l_g = 0.93527,
        a_g = 0.0,
        c_g = 0.56955,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -11.51,
        B = 1357.4,
        C = 0.0088106,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 15,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 81,
    label = "1,1,2,2-tetrachloroethene",
    molecule = "ClC(Cl)=C(Cl)Cl",
    solvent = SolventData(
        s_g = 0.42821,
        b_g = 0.55989,
        e_g = -0.02845,
        l_g = 1.02443,
        a_g = -0.04645,
        c_g = 0.1245,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -1.978,
        B = 555.0,
        C = -1.2216,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 82,
    label = "oxolane",
    molecule = "C1CCOC1",
    solvent = SolventData(
        s_g = 1.33018,
        b_g = -0.03767,
        e_g = -0.492,
        l_g = 1.0155,
        a_g = 3.11944,
        c_g = 0.16482,
        s_h = -17.07744,
        b_h = 3.04258,
        e_h = 4.98498,
        l_h = -8.5809,
        a_h = -42.01867,
        c_h = -5.70097,
        A = -10.335,
        B = 883.6,
        C = -0.05265,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 125,
        dGsolvMAE = (0.17,'kcal/mol'),
        dHsolvCount = 90,
        dHsolvMAE = (0.39,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 83,
    label = "1,2,3,4-tetrahydronaphthalene",
    molecule = "c1ccc2c(c1)CCCC2",
    solvent = SolventData(
        s_g = 1.05459,
        b_g = -1.43576,
        e_g = -0.23041,
        l_g = 1.00834,
        a_g = -0.58503,
        c_g = 0.15803,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -45.327,
        B = 3241.8,
        C = 4.9583,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 20,
        dGsolvMAE = (0.1,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 84,
    label = "tributyl phosphate",
    molecule = "CCCCOP(=O)(OCCCC)OCCCC",
    solvent = SolventData(
        s_g = 1.49741,
        b_g = 1.33253,
        e_g = -0.43108,
        l_g = 1.00757,
        a_g = 5.1522,
        c_g = -1.30418,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 85,
    label = "N,N-diethylethanamine",
    molecule = "CCN(CC)CC",
    solvent = SolventData(
        s_g = 0.42376,
        b_g = -0.0887,
        e_g = -0.29856,
        l_g = 1.006,
        a_g = 3.06973,
        c_g = 0.25515,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -1.033,
        B = 458.2,
        C = -1.4867,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 86,
    label = "1,2,4-trimethylbenzene",
    molecule = "Cc1ccc(C)c(C)c1",
    solvent = SolventData(
        s_g = 1.76422,
        b_g = -1.04965,
        e_g = -0.79671,
        l_g = 0.97318,
        a_g = -0.0,
        c_g = 0.19512,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -7.168,
        B = 1156.0,
        C = -0.6556,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 87,
    label = "1,4-xylene",
    molecule = "Cc1ccc(C)cc1",
    solvent = SolventData(
        s_g = 0.84532,
        b_g = 0.11893,
        e_g = -0.33317,
        l_g = 1.02073,
        a_g = 0.59666,
        c_g = 0.10408,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -5.775,
        B = 826.2,
        C = -0.7739,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "p-Xylene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 129,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 88,
    label = "2-methylpropan-2-ol",
    molecule = "CC(C)(C)O",
    solvent = SolventData(
        s_g = 0.65023,
        b_g = 0.90834,
        e_g = -0.40573,
        l_g = 0.90299,
        a_g = 4.05031,
        c_g = 0.05883,
        s_h = 1.43136,
        b_h = -12.14402,
        e_h = 4.73946,
        l_h = -8.7327,
        a_h = -57.55969,
        c_h = -3.38765,
        A = -216.4,
        B = 13205.0,
        C = 29.254,
        D = -2.4615999999999997e-27,
        E = 10,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 113,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 83,
        dHsolvMAE = (0.41,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 89,
    label = "3-methylbutan-1-ol",
    molecule = "CC(C)CCO",
    solvent = SolventData(
        s_g = 0.65923,
        b_g = 0.91017,
        e_g = -0.41341,
        l_g = 0.92143,
        a_g = 3.65458,
        c_g = -4e-05,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -38.131,
        B = 3773.0,
        C = 3.4876,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 81,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 90,
    label = "undecan-1-ol",
    molecule = "CCCCCCCCCCCO",
    solvent = SolventData(
        s_g = 0.58076,
        b_g = 1.73101,
        e_g = 0.06242,
        l_g = 0.97442,
        a_g = 1.33432,
        c_g = -0.08866,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -83.771,
        B = 6606.1,
        C = 10.065,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 91,
    label = "propan-2-one",
    molecule = "CC(C)=O",
    solvent = SolventData(
        s_g = 1.69516,
        b_g = 0.17306,
        e_g = -0.32032,
        l_g = 0.86014,
        a_g = 2.93123,
        c_g = 0.12029,
        s_h = -16.7202,
        b_h = -4.40072,
        e_h = 2.98338,
        l_h = -6.84571,
        a_h = -34.47063,
        c_h = -5.88329,
        A = -14.918,
        B = 1023.4,
        C = 0.05961,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "Acetone",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 116,
        dGsolvMAE = (0.2,'kcal/mol'),
        dHsolvCount = 87,
        dHsolvMAE = (0.46,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 92,
    label = "methyl acetate",
    molecule = "COC(C)=O",
    solvent = SolventData(
        s_g = 1.69088,
        b_g = 0.19255,
        e_g = -0.38531,
        l_g = 0.86104,
        a_g = 2.62676,
        c_g = 0.15436,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 13.557,
        B = -187.3,
        C = -3.6592,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 87,
        dGsolvMAE = (0.19,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 93,
    label = "propyl acetate",
    molecule = "CCCOC(C)=O",
    solvent = SolventData(
        s_g = 1.06304,
        b_g = 0.47577,
        e_g = -0.1366,
        l_g = 0.89271,
        a_g = 2.45421,
        c_g = 0.24482,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 18.851,
        B = -303.96,
        C = -4.4468,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.17,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 94,
    label = "pentyl acetate",
    molecule = "CCCCCOC(C)=O",
    solvent = SolventData(
        s_g = 0.75079,
        b_g = 0.47914,
        e_g = -0.37424,
        l_g = 1.03007,
        a_g = 2.71499,
        c_g = -0.14138,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -10.639,
        B = 1263.6,
        C = -0.12151,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 95,
    label = "2-methylbutan-2-ol",
    molecule = "CCC(C)(C)O",
    solvent = SolventData(
        s_g = 0.42769,
        b_g = 0.54099,
        e_g = -0.17081,
        l_g = 0.89026,
        a_g = 3.20106,
        c_g = 0.1256,
        s_h = -9.31722,
        b_h = -2.70468,
        e_h = 13.90703,
        l_h = -8.66954,
        a_h = -62.44515,
        c_h = -7.30891,
        A = -195.84,
        B = 11895.0,
        C = 26.385,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 23,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = 22,
        dHsolvMAE = (0.36,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 96,
    label = "4-methylpentan-2-ol",
    molecule = "CC(C)CC(C)O",
    solvent = SolventData(
        s_g = 1.28796,
        b_g = 0.30443,
        e_g = -0.55005,
        l_g = 0.82133,
        a_g = 3.26911,
        c_g = 0.3368,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 54.342,
        B = -4682.3,
        C = -8.9055,
        D = 174970000,
        E = -3,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 15,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 97,
    label = "2-methylpentan-1-ol",
    molecule = "CCCC(C)CO",
    solvent = SolventData(
        s_g = 0.36741,
        b_g = 1.66352,
        e_g = -0.10714,
        l_g = 0.9159,
        a_g = 3.90308,
        c_g = -0.41998,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -70.059,
        B = -5721.1,
        C = 8.4609,
        D = 18893,
        E = -1.1,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 14,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 98,
    label = "2-ethylhexan-1-ol",
    molecule = "CCCCC(CC)CO",
    solvent = SolventData(
        s_g = 0.71109,
        b_g = 0.02229,
        e_g = -0.43734,
        l_g = 0.97233,
        a_g = 3.70508,
        c_g = -0.03541,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -128.56,
        B = 8568.6,
        C = 16.631,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 20,
        dGsolvMAE = (0.21,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 99,
    label = "2-methoxy-2-methylpropane",
    molecule = "COC(C)(C)C",
    solvent = SolventData(
        s_g = 0.78713,
        b_g = -0.11669,
        e_g = -0.4719,
        l_g = 0.99125,
        a_g = 2.8507,
        c_g = 0.29355,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -7.3165,
        B = 810.5,
        C = -0.59662,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 58,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 100,
    label = "dodecan-1-ol",
    molecule = "CCCCCCCCCCCCO",
    solvent = SolventData(
        s_g = -0.24089,
        b_g = 0.85679,
        e_g = 0.38284,
        l_g = 0.98644,
        a_g = 3.39667,
        c_g = -0.20543,
        s_h = 37.43903,
        b_h = 8.72408,
        e_h = -12.9742,
        l_h = -9.53791,
        a_h = -119.92309,
        c_h = -1.21466,
        A = -70.023,
        B = 5998.0,
        C = 8.0302,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.05,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 101,
    label = "2-butoxyethanol",
    molecule = "CCCCOCCO",
    solvent = SolventData(
        s_g = 1.06857,
        b_g = 0.80183,
        e_g = -0.1346,
        l_g = 0.88807,
        a_g = 3.63702,
        c_g = -0.15955,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -5.6874,
        B = 2197.4,
        C = -1.2979,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 102,
    label = "2-ethoxyethanol",
    molecule = "CCOCCO",
    solvent = SolventData(
        s_g = 1.13283,
        b_g = 0.91003,
        e_g = -0.19334,
        l_g = 0.88639,
        a_g = 3.83642,
        c_g = -0.1727,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.653,
        B = 2393.7,
        C = -0.10063,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 26,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 103,
    label = "1-propoxypropane",
    molecule = "CCCOCCC",
    solvent = SolventData(
        s_g = 0.5014,
        b_g = 0.16617,
        e_g = -0.00317,
        l_g = 0.97292,
        a_g = 1.50002,
        c_g = 0.26125,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -8.2119,
        B = 893.52,
        C = 0.022,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 104,
    label = "pentan-2-ol",
    molecule = "CCCC(C)O",
    solvent = SolventData(
        s_g = 0.46762,
        b_g = 1.01443,
        e_g = -0.30386,
        l_g = 0.9319,
        a_g = 3.89726,
        c_g = -0.02451,
        s_h = 1.2695,
        b_h = -5.27753,
        e_h = 5.07207,
        l_h = -8.60835,
        a_h = -70.70626,
        c_h = -6.54809,
        A = -122.33,
        B = 8149.3,
        C = 15.678,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 58,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = 34,
        dHsolvMAE = (0.3,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 105,
    label = "2-methylbutan-1-ol",
    molecule = "CCC(C)CO",
    solvent = SolventData(
        s_g = 0.82358,
        b_g = 0.73546,
        e_g = -1.07594,
        l_g = 1.10639,
        a_g = 3.19871,
        c_g = -0.25016,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -68.504,
        B = 5455.0,
        C = 7.85,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 106,
    label = "pentan-3-ol",
    molecule = "CCC(O)CC",
    solvent = SolventData(
        s_g = 0.22011,
        b_g = 0.79138,
        e_g = -0.10424,
        l_g = 0.8562,
        a_g = 3.80202,
        c_g = 0.11455,
        s_h = 0.37738,
        b_h = -5.35537,
        e_h = 8.79012,
        l_h = -8.53651,
        a_h = -60.73674,
        c_h = -6.01692,
        A = 26.244,
        B = 911.06,
        C = -6.1542,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = 19,
        dHsolvMAE = (0.3,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 107,
    label = "2-propoxyethanol",
    molecule = "CCCOCCO",
    solvent = SolventData(
        s_g = 0.85931,
        b_g = 0.68779,
        e_g = -0.07125,
        l_g = 0.96146,
        a_g = 4.08579,
        c_g = -0.54036,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 108,
    label = "2-propan-2-yloxyethanol",
    molecule = "CC(C)OCCO",
    solvent = SolventData(
        s_g = 0.83732,
        b_g = 0.46411,
        e_g = 0.01452,
        l_g = 0.96999,
        a_g = 4.32879,
        c_g = -0.6685,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 109,
    label = "3-methoxybutan-1-ol",
    molecule = "COC(C)CCO",
    solvent = SolventData(
        s_g = 1.01253,
        b_g = 1.2551,
        e_g = 0.13478,
        l_g = 0.66182,
        a_g = 3.63703,
        c_g = 0.70704,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.13,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 110,
    label = "1-tert-butoxy-2-propanol",
    molecule = "CC(O)COC(C)(C)C",
    solvent = SolventData(
        s_g = 1.10965,
        b_g = 0.00506,
        e_g = -0.58039,
        l_g = 1.07942,
        a_g = 3.8557,
        c_g = -0.70228,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 111,
    label = "2-methoxy-2-methylbutane",
    molecule = "CCC(C)(C)OC",
    solvent = SolventData(
        s_g = 0.504,
        b_g = 0.03943,
        e_g = 0.32158,
        l_g = 1.02616,
        a_g = 2.22194,
        c_g = 0.14583,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -11.276,
        B = 991.96,
        C = -0.018892,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source.
""",
)

entry(
    index = 112,
    label = "pentan-2-one",
    molecule = "CCCC(C)=O",
    solvent = SolventData(
        s_g = -14.76691,
        b_g = 20.21026,
        e_g = 5.19846,
        l_g = 0.93164,
        a_g = -0.0,
        c_g = 0.09677,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.181,
        B = 1147.0,
        C = 0.31253,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 113,
    label = "ethyl butanoate",
    molecule = "CCCC(=O)OCC",
    solvent = SolventData(
        s_g = -13.45737,
        b_g = 18.25613,
        e_g = 4.69803,
        l_g = 0.92582,
        a_g = 0.0,
        c_g = 0.21529,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -15.485,
        B = 1325.6,
        C = 0.6432,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 114,
    label = "heptan-2-one",
    molecule = "CCCCCC(C)=O",
    solvent = SolventData(
        s_g = -12.95934,
        b_g = 17.9718,
        e_g = 4.62621,
        l_g = 0.91635,
        a_g = 0.0,
        c_g = 0.16247,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.565,
        B = 1308.2,
        C = 0.3485,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 115,
    label = "hexyl acetate",
    molecule = "CCCCCCOC(C)=O",
    solvent = SolventData(
        s_g = -13.25703,
        b_g = 18.86058,
        e_g = 4.71488,
        l_g = 0.93318,
        a_g = 0.0,
        c_g = 0.16962,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 116,
    label = "1-nitro-2-octoxybenzene",
    molecule = "CCCCCCCCOc1ccccc1[N+](=O)[O-]",
    solvent = SolventData(
        s_g = 1.47277,
        b_g = 0.81904,
        e_g = 0.16487,
        l_g = 0.79158,
        a_g = 1.19347,
        c_g = -0.2117,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 81,
        dGsolvMAE = (0.3,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 117,
    label = "1-methylpyrrolidin-2-one",
    molecule = "CN1CCCC1=O",
    solvent = SolventData(
        s_g = 2.05547,
        b_g = 0.12822,
        e_g = 0.08961,
        l_g = 0.78018,
        a_g = 4.49382,
        c_g = -0.11795,
        s_h = -24.40451,
        b_h = 5.51139,
        e_h = 20.66699,
        l_h = -8.5427,
        a_h = -48.04472,
        c_h = -3.44818,
        A = -12.503,
        B = 1850.2,
        C = -0.017697,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 127,
        dGsolvMAE = (0.17,'kcal/mol'),
        dHsolvCount = 21,
        dHsolvMAE = (0.62,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 118,
    label = "N-methylacetamide",
    molecule = "CNC(C)=O",
    solvent = SolventData(
        s_g = 1.62919,
        b_g = 0.36038,
        e_g = -0.2321,
        l_g = 0.85148,
        a_g = 4.92155,
        c_g = -0.235,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 55,
        dGsolvMAE = (0.1,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 119,
    label = "morpholine-4-carbaldehyde",
    molecule = "O=CN1CCOCC1",
    solvent = SolventData(
        s_g = 1.9355,
        b_g = 0.78605,
        e_g = 0.43133,
        l_g = 0.69498,
        a_g = 3.67841,
        c_g = -0.37729,
        s_h = 0.54676,
        b_h = -23.51752,
        e_h = -22.55574,
        l_h = -6.68785,
        a_h = -15.91698,
        c_h = 0.96495,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 65,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = 17,
        dHsolvMAE = (0.18,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 120,
    label = "N,N-dibutylformamide",
    molecule = "CCCCN(C=O)CCCC",
    solvent = SolventData(
        s_g = 1.30427,
        b_g = 0.07472,
        e_g = -0.12307,
        l_g = 0.88351,
        a_g = 3.88766,
        c_g = 0.04721,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 41,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 121,
    label = "formamide",
    molecule = "NC=O",
    solvent = SolventData(
        s_g = 2.24092,
        b_g = 1.78587,
        e_g = -0.00272,
        l_g = 0.41666,
        a_g = 4.41662,
        c_g = -0.58509,
        s_h = -6.92729,
        b_h = -23.07347,
        e_h = 3.55662,
        l_h = -7.16221,
        a_h = -29.49074,
        c_h = -5.30108,
        A = -62.009,
        B = 447.02,
        C = 7.2515,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 78,
        dGsolvMAE = (0.15,'kcal/mol'),
        dHsolvCount = 81,
        dHsolvMAE = (0.41,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 122,
    label = "N,N-diethylacetamide",
    molecule = "CCN(CC)C(C)=O",
    solvent = SolventData(
        s_g = 1.65648,
        b_g = 0.1428,
        e_g = -0.1476,
        l_g = 0.87168,
        a_g = 4.56367,
        c_g = -0.00177,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 27,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 123,
    label = "1-methylpiperidin-2-one",
    molecule = "CN1CCCCC1=O",
    solvent = SolventData(
        s_g = 1.97732,
        b_g = 0.191,
        e_g = -0.05682,
        l_g = 0.8891,
        a_g = 4.98342,
        c_g = -0.31184,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 36,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 124,
    label = "N-ethylformamide",
    molecule = "CCNC=O",
    solvent = SolventData(
        s_g = 1.74287,
        b_g = 0.3951,
        e_g = -0.2594,
        l_g = 0.80837,
        a_g = 4.57895,
        c_g = -0.16063,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 26,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 125,
    label = "N-ethylacetamide",
    molecule = "CCNC(C)=O",
    solvent = SolventData(
        s_g = 1.21667,
        b_g = 0.39264,
        e_g = 0.06026,
        l_g = 0.83373,
        a_g = 4.68764,
        c_g = -0.05093,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 33,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 126,
    label = "triolein",
    molecule = "CCCCCCCC/C=C\CCCCCCCC(=O)OCC(COC(=O)CCCCCCC/C=C\CCCCCCCC)OC(=O)CCCCCCC/C=C\CCCCCCCC",
    solvent = SolventData(
        s_g = 0.22861,
        b_g = 0.87324,
        e_g = 0.17311,
        l_g = 0.90303,
        a_g = 0.83268,
        c_g = 0.15358,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 87,
        dGsolvMAE = (0.36,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 127,
    label = "deca-1,9-diene",
    molecule = "C=CCCCCCCC=C",
    solvent = SolventData(
        s_g = -0.49957,
        b_g = 1.40849,
        e_g = 0.07562,
        l_g = 0.98336,
        a_g = 0.34207,
        c_g = 0.00964,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 26,
        dGsolvMAE = (0.23,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 128,
    label = "hexadec-1-ene",
    molecule = "C=CCCCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.09755,
        b_g = 0.05257,
        e_g = 0.03711,
        l_g = 0.99232,
        a_g = 0.28477,
        c_g = -0.04688,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -43.375,
        B = 3289.1,
        C = 4.6393,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 94,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 129,
    label = "1,3-xylene",
    molecule = "Cc1cccc(C)c1",
    solvent = SolventData(
        s_g = 1.00139,
        b_g = -0.00257,
        e_g = -0.37907,
        l_g = 1.01758,
        a_g = 0.54254,
        c_g = 0.08732,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -9.647,
        B = 983.0,
        C = -0.01928,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "m-Xylene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 81,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 130,
    label = "1,2-xylene",
    molecule = "Cc1ccccc1C",
    solvent = SolventData(
        s_g = 0.92629,
        b_g = 0.19207,
        e_g = -0.31782,
        l_g = 1.01746,
        a_g = 0.51918,
        c_g = 0.04592,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -15.678,
        B = 1404.0,
        C = 0.6641,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "o-Xylene",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 61,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 131,
    label = "1,4-dioxane",
    molecule = "C1COCCO1",
    solvent = SolventData(
        s_g = 1.7944,
        b_g = 0.01531,
        e_g = -0.36532,
        l_g = 0.90657,
        a_g = 2.97516,
        c_g = -0.02415,
        s_h = -19.56181,
        b_h = -0.36477,
        e_h = 5.40015,
        l_h = -7.71945,
        a_h = -34.74552,
        c_h = -4.19887,
        A = -36.706,
        B = 2691.5,
        C = 3.6741,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 137,
        dGsolvMAE = (0.18,'kcal/mol'),
        dHsolvCount = 118,
        dHsolvMAE = (0.36,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 132,
    label = "1-chlorobutane",
    molecule = "CCCCCl",
    solvent = SolventData(
        s_g = 0.90664,
        b_g = 0.02496,
        e_g = -0.40444,
        l_g = 0.98621,
        a_g = 0.70786,
        c_g = 0.26487,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 8.91,
        B = 49.58,
        C = -2.9568,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 57,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 133,
    label = "1,1,2,2-tetrabromoethane",
    molecule = "BrC(Br)C(Br)Br",
    solvent = SolventData(
        s_g = 0.205,
        b_g = 1.60401,
        e_g = 1.10605,
        l_g = 0.81585,
        a_g = 0.53612,
        c_g = -0.18218,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -395.22,
        B = 17970,
        C = 58.786,
        D = -0.000054961,
        E = 2,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 134,
    label = "1,1,2,2-tetrachloroethane",
    molecule = "ClC(Cl)C(Cl)Cl",
    solvent = SolventData(
        s_g = 0.22952,
        b_g = 1.77858,
        e_g = 0.781,
        l_g = 0.94058,
        a_g = 0.84434,
        c_g = -0.07845,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -29.579,
        B = 2285.4,
        C = 2.7189,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 135,
    label = "propane-1,2-diol",
    molecule = "CC(O)CO",
    solvent = SolventData(
        s_g = 2.28963,
        b_g = -0.42705,
        e_g = -0.43702,
        l_g = 0.67616,
        a_g = 5.47787,
        c_g = -0.41667,
        s_h = -14.7135,
        b_h = -1.26316,
        e_h = 7.27675,
        l_h = -8.49655,
        a_h = -46.35901,
        c_h = -2.92944,
        A = -293.07,
        B = 17494.0,
        C = 40.576,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = 19,
        dHsolvMAE = (0.1,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 136,
    label = "1,3-dimethylimidazolidin-2-one",
    molecule = "CN1CCN(C)C1=O",
    solvent = SolventData(
        s_g = 1.81674,
        b_g = 0.38939,
        e_g = 0.10789,
        l_g = 0.8109,
        a_g = 4.64145,
        c_g = -0.30057,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 137,
    label = "propane-1,3-diol",
    molecule = "OCCCO",
    solvent = SolventData(
        s_g = 1.1692,
        b_g = 0.75617,
        e_g = 0.45259,
        l_g = 0.60581,
        a_g = 4.63421,
        c_g = -0.40968,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -57.427,
        B = 5623.9,
        C = 6.2001,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 138,
    label = "butane-1,4-diol",
    molecule = "OCCCCO",
    solvent = SolventData(
        s_g = 0.43797,
        b_g = 1.73876,
        e_g = 0.76809,
        l_g = 0.60858,
        a_g = 4.38218,
        c_g = -0.17545,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -76.012,
        B = 6966.8,
        C = 8.7765,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 139,
    label = "pentane-1,5-diol",
    molecule = "OCCCCCO",
    solvent = SolventData(
        s_g = -0.39893,
        b_g = 3.52249,
        e_g = 0.9632,
        l_g = 0.69625,
        a_g = 2.5135,
        c_g = -0.3546,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -76.248,
        B = 7080.9,
        C = 8.8187,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 140,
    label = "1-bromonaphthalene",
    molecule = "Brc1cccc2ccccc12",
    solvent = SolventData(
        s_g = 0.91909,
        b_g = 0.49103,
        e_g = 0.15934,
        l_g = 0.86216,
        a_g = 0.94625,
        c_g = 0.01742,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 141,
    label = "1-chloronaphthalene",
    molecule = "Clc1cccc2ccccc12",
    solvent = SolventData(
        s_g = -0.76995,
        b_g = 0.12984,
        e_g = 1.44727,
        l_g = 1.00069,
        a_g = 0.0,
        c_g = -0.33148,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 9.2058,
        B = 1134.0,
        C = -3.3047,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 142,
    label = "dec-1-ene",
    molecule = "C=CCCCCCCCC",
    solvent = SolventData(
        s_g = -13.77923,
        b_g = 10.52025,
        e_g = 4.75674,
        l_g = 0.97507,
        a_g = 55.48955,
        c_g = 0.2317,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -15.858,
        B = 1430.5,
        C = 0.68113,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 143,
    label = "hex-1-ene",
    molecule = "C=CCCCC",
    solvent = SolventData(
        s_g = 0.13822,
        b_g = 0.28251,
        e_g = -0.51018,
        l_g = 1.00075,
        a_g = 0.06344,
        c_g = 0.28234,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -6.909,
        B = 656.9,
        C = -0.062835,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 144,
    label = "1-nitropropane",
    molecule = "CCC[N+](=O)[O-]",
    solvent = SolventData(
        s_g = 1.50765,
        b_g = 1.28832,
        e_g = -0.08106,
        l_g = 0.8041,
        a_g = 0.0,
        c_g = 0.17553,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -24.521,
        B = 1788.6,
        C = 1.9988,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 145,
    label = "oct-1-ene",
    molecule = "C=CCCCCCC",
    solvent = SolventData(
        s_g = -17.42443,
        b_g = 12.83873,
        e_g = 5.97004,
        l_g = 1.00831,
        a_g = 73.77575,
        c_g = 0.17757,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 15.841,
        B = -194.4,
        C = -4.018,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 146,
    label = "2-sulfanylethanol",
    molecule = "OCCS",
    solvent = SolventData(
        s_g = 1.00047,
        b_g = 1.93431,
        e_g = 0.60278,
        l_g = 0.691,
        a_g = 3.11754,
        c_g = -0.43075,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 147,
    label = "3-methylthiolane 1,1-dioxide",
    molecule = "CC1CCS(=O)(=O)C1",
    solvent = SolventData(
        s_g = 2.91218,
        b_g = -0.90316,
        e_g = -0.07112,
        l_g = 0.71957,
        a_g = 2.02325,
        c_g = -0.3364,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -72.515,
        B = 5360.1,
        C = 8.7917,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 148,
    label = "hexanedinitrile",
    molecule = "N#CCCCCC#N",
    solvent = SolventData(
        s_g = 1.33529,
        b_g = 2.93914,
        e_g = 0.47315,
        l_g = 0.75883,
        a_g = 5.12869,
        c_g = -0.63501,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -18.181,
        B = 2014.8,
        C = 1.0968,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 149,
    label = "benzyl acetate",
    molecule = "CC(=O)OCc1ccccc1",
    solvent = SolventData(
        s_g = 1.21772,
        b_g = 0.66574,
        e_g = 0.14372,
        l_g = 0.87976,
        a_g = 2.69437,
        c_g = -0.09201,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -18.431,
        B = 2179.5,
        C = 0.865,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 150,
    label = "cyclohexylcyclohexane",
    molecule = "C1CCC(C2CCCCC2)CC1",
    solvent = SolventData(
        s_g = -0.61183,
        b_g = 0.37019,
        e_g = 0.47242,
        l_g = 0.94953,
        a_g = 0.94623,
        c_g = 0.23128,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = 24.519,
        B = -9629.1,
        C = -0.38364,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 151,
    label = "butanenitrile",
    molecule = "CCCC#N",
    solvent = SolventData(
        s_g = 2.31213,
        b_g = -0.20123,
        e_g = -0.66216,
        l_g = 0.8891,
        a_g = 2.7938,
        c_g = -0.06015,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -7.7634,
        B = 925.92,
        C = -0.49345,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 25,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 152,
    label = "cis-1,2-dichloroethene",
    molecule = "Cl/C=C\Cl",
    solvent = SolventData(
        s_g = 0.61086,
        b_g = 0.91679,
        e_g = -0.1365,
        l_g = 1.05819,
        a_g = 0.2456,
        c_g = 0.12124,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -13.508,
        B = 964.23,
        C = 0.44868,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 153,
    label = "cis-decaline",
    molecule = "C1CC[C@H]2CCCC[C@H]2C1",
    solvent = SolventData(
        s_g = 0.26567,
        b_g = 0.10948,
        e_g = -0.2302,
        l_g = 1.03696,
        a_g = 0.0,
        c_g = 0.01578,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -44.032,
        B = 3379.6,
        C = 4.7234,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 19,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 154,
    label = "cyclohexanol",
    molecule = "OC1CCCCC1",
    solvent = SolventData(
        s_g = -8.24639,
        b_g = 17.62908,
        e_g = 3.70331,
        l_g = 0.91097,
        a_g = -13.05371,
        c_g = -0.15469,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -87.257,
        B = 7419.6,
        C = 10.327,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 155,
    label = "cyclohexylbenzene",
    molecule = "c1ccc(C2CCCCC2)cc1",
    solvent = SolventData(
        s_g = 0.00051,
        b_g = 0.71012,
        e_g = 0.28745,
        l_g = 1.00324,
        a_g = 2.02234,
        c_g = -0.00919,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -12.051,
        B = 1819.4,
        C = 0,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 156,
    label = "cyclopentanone",
    molecule = "O=C1CCCC1",
    solvent = SolventData(
        s_g = -0.02313,
        b_g = 2.01236,
        e_g = 0.32827,
        l_g = 0.98855,
        a_g = 9.24619,
        c_g = -0.06679,
        s_h = 3.99827,
        b_h = -26.54762,
        e_h = -1.90582,
        l_h = -8.00511,
        a_h = -142.42979,
        c_h = -3.09625,
        A = -23.53,
        B = 5012.0,
        C = 0,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = 16,
        dHsolvMAE = (0.06,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 157,
    label = "deuterated water",
    molecule = "[2H]O[2H]",
    solvent = SolventData(
        s_g = 2.4615,
        b_g = 4.28228,
        e_g = 0.83887,
        l_g = -0.15639,
        a_g = 4.13302,
        c_g = -0.98972,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 69,
        dGsolvMAE = (0.18,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 158,
    label = "bis(2-ethylhexyl) hexanedioate",
    molecule = "CCCCC(CC)COC(=O)CCCCC(=O)OCC(CC)CCCC",
    solvent = SolventData(
        s_g = 3.17646,
        b_g = -3.3948,
        e_g = -1.15624,
        l_g = 0.70313,
        a_g = 3.46268,
        c_g = 0.72829,
        s_h = -39.34604,
        b_h = 45.27509,
        e_h = 16.99983,
        l_h = -5.85499,
        a_h = -44.90653,
        c_h = -12.84426,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.18,'kcal/mol'),
        dHsolvCount = 21,
        dHsolvMAE = (0.44,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 159,
    label = "2,2-dichloroacetic acid",
    molecule = "O=C(O)C(Cl)Cl",
    solvent = SolventData(
        s_g = 0.01233,
        b_g = 2.04468,
        e_g = 0.97722,
        l_g = 0.89087,
        a_g = 2.46663,
        c_g = -0.36831,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 160,
    label = "diethyl benzene-1,2-dicarboxylate",
    molecule = "CCOC(=O)c1ccccc1C(=O)OCC",
    solvent = SolventData(
        s_g = 1.71569,
        b_g = 0.20205,
        e_g = -0.14121,
        l_g = 0.84214,
        a_g = 2.18408,
        c_g = -0.20108,
        s_h = -13.18857,
        b_h = -6.83214,
        e_h = 2.04035,
        l_h = -7.95025,
        a_h = -26.24228,
        c_h = -1.10161,
        A = -14.11,
        B = 2851.0,
        C = 0,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 31,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = 13,
        dHsolvMAE = (0.17,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 161,
    label = "2-(2-hydroxyethoxy)ethanol",
    molecule = "OCCOCCO",
    solvent = SolventData(
        s_g = 1.80371,
        b_g = 1.402,
        e_g = 0.26276,
        l_g = 0.63336,
        a_g = 4.68302,
        c_g = -0.65618,
        s_h = -8.06601,
        b_h = -34.64865,
        e_h = 1.0923,
        l_h = -6.06505,
        a_h = -22.01269,
        c_h = -2.85078,
        A = -62.425,
        B = 5966.9,
        C = 6.8296,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 56,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = 16,
        dHsolvMAE = (0.54,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source. 
""",
)

entry(
    index = 162,
    label = "1-ethoxy-2-(2-ethoxyethoxy)ethane",
    molecule = "CCOCCOCCOCC",
    solvent = SolventData(
        s_g = 2.12002,
        b_g = -0.86531,
        e_g = -0.59725,
        l_g = 0.9525,
        a_g = 3.82094,
        c_g = -0.07032,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 163,
    label = "1-methoxy-2-(2-methoxyethoxy)ethane",
    molecule = "COCCOCCOC",
    solvent = SolventData(
        s_g = 0.99865,
        b_g = 0.59136,
        e_g = -0.35265,
        l_g = 0.91477,
        a_g = 6.1889,
        c_g = -0.0855,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -12.272,
        B = 1422.3,
        C = 0.10585,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 164,
    label = "diiodomethane",
    molecule = "ICI",
    solvent = SolventData(
        s_g = 1.02264,
        b_g = 0.89843,
        e_g = 1.47668,
        l_g = 0.74636,
        a_g = 0.35558,
        c_g = -0.38941,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -34.41,
        B = 241.96,
        C = 3.5698,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 165,
    label = "dibutyl benzene-1,2-dicarboxylate",
    molecule = "CCCCOC(=O)c1ccccc1C(=O)OCCCC",
    solvent = SolventData(
        s_g = 1.05461,
        b_g = 0.29007,
        e_g = -0.00181,
        l_g = 0.85846,
        a_g = 2.03696,
        c_g = 0.12025,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -250.53,
        B = 14426.0,
        C = 34.706,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 15,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 166,
    label = "dinonyl benzene-1,2-dicarboxylate",
    molecule = "CCCCCCCCCOC(=O)c1ccccc1C(=O)OCCCCCCCCC",
    solvent = SolventData(
        s_g = -3.09707,
        b_g = 0.51717,
        e_g = 3.24168,
        l_g = 0.97978,
        a_g = 3.89549,
        c_g = -0.2515,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 167,
    label = "bis(2-ethylhexyl) phthalate",
    molecule = "CCCCC(CC)COC(=O)c1ccccc1C(=O)OCC(CC)CCCC",
    solvent = SolventData(
        s_g = 0.6464,
        b_g = -0.37408,
        e_g = 0.19661,
        l_g = 0.88781,
        a_g = 3.02399,
        c_g = -0.01824,
        s_h = -8.33767,
        b_h = -3.57747,
        e_h = 3.75614,
        l_h = -8.27821,
        a_h = 0.0,
        c_h = -3.96357,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 11,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.12,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 168,
    label = "3-(3-hydroxypropoxy)propan-1-ol",
    molecule = "OCCCOCCCO",
    solvent = SolventData(
        s_g = 1.44969,
        b_g = 0.13747,
        e_g = 0.22552,
        l_g = 0.83553,
        a_g = 2.14692,
        c_g = -0.44041,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 169,
    label = "ethane-1,2-diol",
    molecule = "OCCO",
    solvent = SolventData(
        s_g = 2.27301,
        b_g = 1.10258,
        e_g = -0.06179,
        l_g = 0.54103,
        a_g = 5.34026,
        c_g = -0.84237,
        s_h = -11.73905,
        b_h = -8.01831,
        e_h = -4.82369,
        l_h = -6.23321,
        a_h = -44.28415,
        c_h = -3.22667,
        A = -103.52,
        B = 7563.0,
        C = 13.009,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 53,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 25,
        dHsolvMAE = (0.78,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht. NOTE: Typo corrected from original source. 
""",
)

entry(
    index = 170,
    label = "furan-2-carbaldehyde",
    molecule = "O=Cc1ccco1",
    solvent = SolventData(
        s_g = 0.96881,
        b_g = 3.05671,
        e_g = 0.25523,
        l_g = 0.77784,
        a_g = 4.10348,
        c_g = -0.32828,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -69.008,
        B = 3950.4,
        C = 8.655,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 171,
    label = "furan-2-ylmethanol",
    molecule = "OCc1ccco1",
    solvent = SolventData(
        s_g = 1.67116,
        b_g = 0.4943,
        e_g = 0.21862,
        l_g = 0.82156,
        a_g = 3.98036,
        c_g = -0.49784,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -37.008,
        B = 3555.0,
        C = 3.4664,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 172,
    label = "oxolan-2-one",
    molecule = "O=C1CCCO1",
    solvent = SolventData(
        s_g = 2.68701,
        b_g = -0.1148,
        e_g = -0.06359,
        l_g = 0.6827,
        a_g = 3.65486,
        c_g = -0.1692,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 23,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 173,
    label = "1H-indene",
    molecule = "C1=Cc2ccccc2C1",
    solvent = SolventData(
        s_g = 0.27525,
        b_g = -0.02319,
        e_g = 0.70179,
        l_g = 0.9297,
        a_g = 0.0,
        c_g = 0.02898,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -18.972,
        B = 1929.9,
        C = 1.0707,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 174,
    label = "2-aminoethanol",
    molecule = "NCCO",
    solvent = SolventData(
        s_g = 1.53429,
        b_g = 0.68228,
        e_g = 0.94825,
        l_g = 0.58841,
        a_g = 6.3679,
        c_g = -0.88936,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -8.583,
        B = 3152.0,
        C = -1.0266,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 22,
        dGsolvMAE = (0.06,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 175,
    label = "1-ethylpyrrolidin-2-one",
    molecule = "CCN1CCCC1=O",
    solvent = SolventData(
        s_g = 1.79889,
        b_g = 0.10918,
        e_g = 0.14087,
        l_g = 0.8415,
        a_g = 5.06353,
        c_g = -0.09604,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 23,
        dGsolvMAE = (0.07,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 176,
    label = "tetradecane",
    molecule = "CCCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = -0.36094,
        b_g = 0.52976,
        e_g = 0.22467,
        l_g = 0.9831,
        a_g = 1.08505,
        c_g = 0.05999,
        s_h = -3.37063,
        b_h = -1.57818,
        e_h = 6.51703,
        l_h = -9.12045,
        a_h = -4.27501,
        c_h = -6.93941,
        A = -20.486,
        B = 2088.4,
        C = 1.2852,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 21,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = 22,
        dHsolvMAE = (0.33,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 177,
    label = "tridecane",
    molecule = "CCCCCCCCCCCCC",
    solvent = SolventData(
        s_g = 0.08172,
        b_g = -0.07718,
        e_g = 0.08018,
        l_g = 0.9907,
        a_g = -0.09899,
        c_g = 0.09537,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.01,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 178,
    label = "octamethylcyclotetrasiloxane",
    molecule = "C[Si]1(C)O[Si](C)(C)O[Si](C)(C)O[Si](C)(C)O1",
    solvent = SolventData(
        s_g = 1.77556,
        b_g = 4.33929,
        e_g = -0.95093,
        l_g = 0.91268,
        a_g = 0.21782,
        c_g = 0.20416,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "D4",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 179,
    label = "perflexane",
    molecule = "FC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)F",
    solvent = SolventData(
        s_g = -0.44688,
        b_g = 0.71818,
        e_g = -0.4199,
        l_g = 0.51144,
        a_g = -1.17023,
        c_g = 0.71204,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 18,
        dGsolvMAE = (0.14,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 180,
    label = "perfluorooctane",
    molecule = "FC(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)C(F)(F)F",
    solvent = SolventData(
        s_g = -7.94397,
        b_g = -16.30332,
        e_g = 2.54941,
        l_g = 0.66865,
        a_g = -0.0,
        c_g = 0.09721,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 181,
    label = "2-phenylacetonitrile",
    molecule = "N#CCc1ccccc1",
    solvent = SolventData(
        s_g = 0.4927,
        b_g = 2.71631,
        e_g = 0.58287,
        l_g = 1.00108,
        a_g = 0.0,
        c_g = -0.71915,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -25.663,
        B = 2207.1,
        C = 2.1116,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 182,
    label = "propanenitrile",
    molecule = "CCC#N",
    solvent = SolventData(
        s_g = 2.17242,
        b_g = 0.09059,
        e_g = -0.27225,
        l_g = 0.77038,
        a_g = -2.58108,
        c_g = 0.24229,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -5.7136,
        B = 703.6,
        C = -0.78123,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 22,
        dGsolvMAE = (0.12,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 183,
    label = "4-methyl-1,3-dioxolan-2-one",
    molecule = "CC1COC(=O)O1",
    solvent = SolventData(
        s_g = 3.15302,
        b_g = -0.09687,
        e_g = -0.61225,
        l_g = 0.70877,
        a_g = 3.33033,
        c_g = -0.37072,
        s_h = -16.08778,
        b_h = -11.51353,
        e_h = 1.91472,
        l_h = -6.51177,
        a_h = -17.84913,
        c_h = -4.22151,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 39,
        dGsolvMAE = (0.16,'kcal/mol'),
        dHsolvCount = 113,
        dHsolvMAE = (0.46,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 184,
    label = "quinoline",
    molecule = "c1ccc2ncccc2c1",
    solvent = SolventData(
        s_g = 1.10867,
        b_g = 0.4956,
        e_g = 0.22457,
        l_g = 0.85655,
        a_g = 3.37876,
        c_g = 0.00456,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -51.162,
        B = 3942.4,
        C = 5.6579,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 29,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 185,
    label = "2-chlorobutane",
    molecule = "CCC(C)Cl",
    solvent = SolventData(
        s_g = 1.02846,
        b_g = -0.02593,
        e_g = -1.32513,
        l_g = 0.93204,
        a_g = 3.84033,
        c_g = 0.45323,
        s_h = -0.70075,
        b_h = -0.56283,
        e_h = 6.42173,
        l_h = -8.84955,
        a_h = 0.0,
        c_h = -8.24864,
        A = -42.417,
        B = 2410.5,
        C = 4.6466,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 8,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = 8,
        dHsolvMAE = (0.04,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 186,
    label = "squalane",
    molecule = "CC(C)CCCC(C)CCCC(C)CCCCC(C)CCCC(C)CCCC(C)C",
    solvent = SolventData(
        s_g = 0.28485,
        b_g = -0.17076,
        e_g = -0.14957,
        l_g = 0.97416,
        a_g = 0.0,
        c_g = -0.04211,
        s_h = -10.53039,
        b_h = 7.8714,
        e_h = 8.38144,
        l_h = -7.42254,
        a_h = 3.14948,
        c_h = -8.38603,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 41,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = 25,
        dHsolvMAE = (0.18,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 187,
    label = "tetraethylene glycol",
    molecule = "OCCOCCOCCOCCO",
    solvent = SolventData(
        s_g = 1.3414,
        b_g = 1.44335,
        e_g = 0.57393,
        l_g = 0.68468,
        a_g = 1.74944,
        c_g = -0.57574,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -18.728,
        B = 4056.8,
        C = 0.34542,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 16,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 188,
    label = "tetraglyme",
    molecule = "COCCOCCOCCOCCOC",
    solvent = SolventData(
        s_g = 1.22215,
        b_g = 0.51311,
        e_g = -0.12957,
        l_g = 0.84506,
        a_g = 5.59973,
        c_g = -0.18184,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 189,
    label = "thiodiglycol",
    molecule = "OCCSCCO",
    solvent = SolventData(
        s_g = -2.05002,
        b_g = 9.51053,
        e_g = 1.36088,
        l_g = 0.5325,
        a_g = -6.90194,
        c_g = -0.24616,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 190,
    label = "trans-1,2-dichloroethene",
    molecule = "Cl/C=C/Cl",
    solvent = SolventData(
        s_g = 0.56394,
        b_g = 0.67954,
        e_g = -0.09174,
        l_g = 1.13617,
        a_g = 1.25327,
        c_g = -0.07564,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -14.078,
        B = 981.81,
        C = 0.513,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.08,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 191,
    label = "trans-decalin",
    molecule = "C1CC[C@H]2CCCC[C@@H]2C1",
    solvent = SolventData(
        s_g = 0.62739,
        b_g = -0.29334,
        e_g = -0.30332,
        l_g = 0.97922,
        a_g = 0.21566,
        c_g = 0.16573,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -28.692,
        B = 2396.7,
        C = 2.5297,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 14,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 192,
    label = "N,N-dipentylpentan-1-amine",
    molecule = "CCCCCN(CCCCC)CCCCC",
    solvent = SolventData(
        s_g = -0.29376,
        b_g = -0.20942,
        e_g = 0.50285,
        l_g = 0.90351,
        a_g = 2.15054,
        c_g = 0.26141,
        s_h = 2.40166,
        b_h = 11.58811,
        e_h = -0.50176,
        l_h = -10.4943,
        a_h = -56.48737,
        c_h = -2.89836,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.06,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 193,
    label = "tricaprylin",
    molecule = "CCCCCCCC(=O)OCC(COC(=O)CCCCCCC)OC(=O)CCCCCCC",
    solvent = SolventData(
        s_g = 0.82081,
        b_g = 1.47908,
        e_g = -0.07952,
        l_g = 0.92604,
        a_g = 4.0725,
        c_g = -0.13206,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 17,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 194,
    label = "triethyl phosphate",
    molecule = "CCOP(=O)(OCC)OCC",
    solvent = SolventData(
        s_g = 0.1189,
        b_g = 0.55442,
        e_g = -0.97631,
        l_g = 0.77934,
        a_g = 3.34021,
        c_g = 1.0203,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 13,
        dGsolvMAE = (0.02,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 195,
    label = "triethylene glycol",
    molecule = "OCCOCCOCCO",
    solvent = SolventData(
        s_g = 1.44217,
        b_g = 1.00619,
        e_g = 0.67914,
        l_g = 0.67162,
        a_g = 4.36505,
        c_g = -0.68698,
        s_h = 3.42969,
        b_h = -41.46433,
        e_h = -14.21714,
        l_h = -4.54942,
        a_h = -8.7017,
        c_h = -3.1873,
        A = -99.75,
        B = 7640.0,
        C = 12.43,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 34,
        dGsolvMAE = (0.09,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.05,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 196,
    label = "triglyme",
    molecule = "COCCOCCOCCOC",
    solvent = SolventData(
        s_g = 1.86546,
        b_g = 0.17264,
        e_g = -0.23118,
        l_g = 0.88096,
        a_g = 4.39932,
        c_g = -0.22892,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 12,
        dGsolvMAE = (0.05,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 197,
    label = "N,N-dibutylbutan-1-amine",
    molecule = "CCCCN(CCCC)CCCC",
    solvent = SolventData(
        s_g = -0.32536,
        b_g = 0.13687,
        e_g = 0.39488,
        l_g = 0.96903,
        a_g = 2.32072,
        c_g = 0.04705,
        s_h = 4.53557,
        b_h = 2.02601,
        e_h = -0.71163,
        l_h = -9.68255,
        a_h = -49.04689,
        c_h = -6.09563,
        A = -28.279,
        B = 2355.1,
        C = 2.4141,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 10,
        dGsolvMAE = (0.03,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.09,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): the DIPPR, version 2023.
""",
)

entry(
    index = 198,
    label = "N,N-dioctyloctan-1-amine",
    molecule = "CCCCCCCCN(CCCCCCCC)CCCCCCCC",
    solvent = SolventData(
        s_g = -0.3707,
        b_g = 0.36622,
        e_g = 0.60141,
        l_g = 0.86702,
        a_g = 1.7667,
        c_g = 0.22219,
        s_h = 15.98697,
        b_h = -62.11023,
        e_h = -9.18597,
        l_h = -4.37492,
        a_h = -19.58048,
        c_h = -16.39085,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 9,
        dGsolvMAE = (0.04,'kcal/mol'),
        dHsolvCount = 9,
        dHsolvMAE = (0.16,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham and Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 199,
    label = "hexamethylphosphoramide",
    molecule = "CN(C)P(=O)(N(C)C)N(C)C",
    solvent = SolventData(
        s_g = 2.583,
        b_g = -0.88196,
        e_g = -0.43921,
        l_g = 0.88314,
        a_g = 7.36045,
        c_g = -0.12452,
        s_h = None,
        b_h = None,
        e_h = None,
        l_h = None,
        a_h = None,
        c_h = None,
        A = -51.263,
        B = 3610.7,
        C = 5.8603,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = 33,
        dGsolvMAE = (0.11,'kcal/mol'),
        dHsolvCount = None,
        dHsolvMAE = None,
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Abraham parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

entry(
    index = 200,
    label = "dimethyl carbonate",
    molecule = "COC(=O)OC",
    solvent = SolventData(
        s_g = None,
        b_g = None,
        e_g = None,
        l_g = None,
        a_g = None,
        c_g = None,
        s_h = -17.43963,
        b_h = -2.99216,
        e_h = 6.67692,
        l_h = -8.18497,
        a_h = -28.87129,
        c_h = -3.10893,
        A = None,
        B = None,
        C = None,
        D = None,
        E = None,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = "DimethylCarbonate",
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = None,
        dGsolvMAE = None,
        dHsolvCount = 59,
        dHsolvMAE = (0.42,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
""",
)

entry(
    index = 201,
    label = "diethyl carbonate",
    molecule = "CCOC(=O)OCC",
    solvent = SolventData(
        s_g = None,
        b_g = None,
        e_g = None,
        l_g = None,
        a_g = None,
        c_g = None,
        s_h = -16.14978,
        b_h = -0.17336,
        e_h = 6.62452,
        l_h = -8.74529,
        a_h = -25.49243,
        c_h = -4.31324,
        A = -47.078,
        B = 2783.2,
        C = 5.3617,
        D = 0,
        E = 0,
        alpha = None,
        beta = None,
        eps = None,
        name_in_coolprop = None,
    ),
    dataCount = DataCountSolvent(
        dGsolvCount = None,
        dGsolvMAE = None,
        dHsolvCount = 80,
        dHsolvMAE = (0.29,'kcal/mol'),
    ),
    shortDesc = u""" """,
    longDesc = 
u"""
Mintz parameters: fitted by Chung, Y., Vermeire, F. H., Wu, H., Walker, P. J., Abraham, M. H., 
& Green, W. H. (2022). J. Chem. Inf. Model, 62(3), 433-446.
Viscosity parameters (A, B, C, D, E): Viswanath, D. S., Ghosh, T. K., Prasad, D. H. L., Dutt, N. V. K.,
Rani, K. Y. (2007) Viscosity of Liquids. Springer, The Netherlands: Dordrecht.
""",
)

