#!/usr/bin/env python
# encoding: utf-8

name = "KlippensteinH2O2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H + O2 <=> O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+14, 'cm^3/(mol*s)'), n=0, Ea=(15286, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
!<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>!
!
!                     ----- H2 Kinetic Mechanism -----
!                     -----   Version 6-10-2011  -----
!
! (c) Burke, Chaos, Ju, Dryer, and Klippenstein; Princeton University, 2011.
!
!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!
!  HOW TO USE THIS MECHANISM:
!
! (*) Due to limitations of CHEMKIN-II format (specifically, an inability to
!     implement temperature-dependent collision efficiencies in falloff
!     reactions) and the lack of fundamental understanding of the mixing rules
!     for the falloff reactions with the bath gases that have different
!     broadening factors, the present implementation represents a compromise
!     (approximate) formulation.  As a consequence,
!
!     PRIOR TO ITS USE IN THE CALCULATIONS, THIS FILE HAS TO BE MODIFIED.
!     DEPENDING ON WHAT BATH GAS (DILUTANT) IS MOST ABUNDANT IN YOUR SYSTEM
!     (THE PRESENT CHOICES ARE N2, AR, OR HE),  YOU  SHOULD UNCOMMENT THE
!     CORRESPONDING BLOCK FOR THE REACTION H+O2(+M)=HO2(+M), AND COMMENT THE
!     BLOCK FOR OTHER DILUTANT(S).  AS GIVEN, THE MAIN DILUTANT IS SET TO BE N2.
!
!
!  HOW TO REFERENCE THIS MECHANISM:
!
!     M.P. Burke, M. Chaos, Y. Ju, F.L. Dryer, S.J. Klippenstein
!        "Comprehensive H2/O2 Kinetic Model for High-Pressure Combustion,"
!        Int. J. Chem. Kinet. (2011).
!
!  FUTURE REVISIONS/UPDATES MAY BE FOUND ON THE FUELS AND COMBUSTION RESEARCH LABORATORY
!  WEBSITE: < http://www.princeton.edu/mae/people/faculty/dryer/homepage/combustion_lab/ >
!
!
!  HOW TO CONTACT THE AUTHORS:
!
!     Dr. Michael P. Burke
!     R122 Building 200
!     Chemical Sciences and Engineering Division
!     Argonne National Laboratory
!     Argonne, IL 60439
!     Email: mpburke@anl.gov
!
!     Prof. Frederick L. Dryer
!     D-329D Engineering Quadrangle
!     Mechanical and Aerospace Engineering
!     Princeton University
!     Princeton, NJ 08544
!     Phone: 609-258-5206
!     Lab:   609-258-0316
!     FAX:   609-258-1939
!     Email: fldryer@princeton.edu
!
!
!<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>!
!
ELEMENTS
H O N AR HE C
END


!======================
!H2-O2 Chain Reactions
!======================
! Hong et al., Proc. Comb. Inst. 33:309-316 (2011)
""",
)

entry(
    index = 2,
    label = "O + H2 <=> H + OH",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.818e+12, 'cm^3/(mol*s)'), n=0, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (8.792e+14, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19170, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)
""",
)

entry(
    index = 4,
    label = "H2 + OH <=> H2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.16e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
! Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)
""",
)

entry(
    index = 5,
    label = "OH + OH <=> O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(33400, 'cm^3/(mol*s)'), n=2.42, Ea=(-1930, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)
""",
)

entry(
    index = 6,
    label = "H2O + H2O <=> H + OH + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120180, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
!============================
!H2-O2 Dissociation Reactions
!============================
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
H2+AR = H+H+AR                                  5.840E+18 -1.10  1.0438E+05
H2+HE = H+H+HE                                  5.840E+18 -1.10  1.0438E+05
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
O+O+AR = O2+AR                                  1.886E+13  0.00 -1.788E+03
O+O+HE = O2+HE                                  1.886E+13  0.00 -1.788E+03
! Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)
""",
)

entry(
    index = 7,
    label = "HO2 + H <=> H2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75e+06, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1451, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
!=================================
! Formation and consumption of HO2
!=================================

! High-pressure limit from Troe, Proc. Comb. Inst. 28:1463-1469 (2000)
! Low-pressure  limit from Michael et al., J. Phys. Chem. A 106:5297-5313
! Centering factors from Fernandes et al., Phys. Chem. Chem. Phys. 10:4313-4321 (2008)
!=================================================================================
! Michael et al., Proc. Comb. Inst. 28:1471 (2000)
!HO2+H = H2+O2                                     3.659E+06  2.09 -1.451E+03
!Scaled by 0.75
""",
)

entry(
    index = 8,
    label = "HO2 + H <=> OH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.079e+13, 'cm^3/(mol*s)'), n=0, Ea=(295, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
! Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)
""",
)

entry(
    index = 9,
    label = "HO2 + O <=> O2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.85e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-723.93, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
! Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)
!HO2+O = O2+OH                                   4.750E+11  1.00 -7.2393E+02
!Scaled by 0.60
""",
)

entry(
    index = 10,
    label = "HO2 + OH <=> H2O + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.89e+13, 'cm^3/(mol*s)'), n=0, Ea=(-497, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
! Keyser, J. Phys. Chem. 92:1193 (1988)
""",
)

entry(
    index = 11,
    label = "HO2 + HO2 <=> H2O2 + O2",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(4.2e+14, 'cm^3/(mol*s)'), n=0, Ea=(11982, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (1.3e+11, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1629.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    longDesc = 
u"""
!=====================================
!Formation and Consumption of H2O2
!=====================================
! Hippler et al., J. Chem. Phys. 93:1755 (1990)
""",
)

entry(
    index = 13,
    label = "H2O2 + H <=> H2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.41e+13, 'cm^3/(mol*s)'), n=0, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 14,
    label = "H2O2 + H <=> HO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.82e+13, 'cm^3/(mol*s)'), n=0, Ea=(7950, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "H2O2 + O <=> OH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.55e+06, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "H2O2 + OH <=> HO2 + H2O",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.74e+12, 'cm^3/(mol*s)'), n=0, Ea=(318, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.59e+13, 'cm^3/(mol*s)'), n=0, Ea=(7270, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    longDesc = 
u"""
! Hong et al., J. Phys. Chem. A  114 (2010) 5718-5727
""",
)

entry(
    index = 18,
    label = "H2 <=> H + H",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104380, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C]=O': 1.9, '[Ar]': 0},
    ),
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 19,
    label = "O + O <=> O2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.165e+15, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0, '[C]=O': 1.9, '[Ar]': 0},
    ),
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 20,
    label = "O + H <=> OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
    ),
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 21,
    label = "H2O <=> H + OH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.064e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120790, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 0, '[H][H]': 3, '[He]': 1.1, '[O][O]': 1.5, 'N#N': 2, '[C]=O': 1.9},
    ),
    longDesc = 
u"""
! Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)
! Rate constant is for Ar with efficiencies from Michael et al., J. Phys. Chem. A, 106 (2002)
""",
)

entry(
    index = 22,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.65084e+12, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (9.042e+19, 'cm^6/(mol^2*s)'),
            n = -1.5,
            Ea = (492.2, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=C=O': 3.8, 'O': 14, '[H][H]': 2, '[He]': 0.8, '[O][O]': 0.78, '[C]=O': 1.9, '[Ar]': 0.67},
    ),
    longDesc = 
u"""
! Efficiencies for CO and CO2 taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
! MAIN BATH GAS IS N2 (comment this reaction otherwise)
!
""",
)

entry(
    index = 23,
    label = "H2O2 <=> OH + OH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2e+12, 's^-1'), n=0.9, Ea=(48749, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.49e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.5, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, 'N#N': 1.5, '[C]=O': 2.8},
    ),
    longDesc = 
u"""
!=================================================================================
! MAIN BATH GAS IS AR OR HE (comment this reaction otherwise)
!
!H + O2 (+M) <=> HO2 (+M)      4.65084E+12  0.44  0.000E+00    0.0 0.0 0.0
!H2/ 3.0/ H2O/ 21/ O2/ 1.1/ CO/ 2.7/ CO2/ 5.4/ HE/ 1.2/ N2/ 1.5/
!=================================================================================
! Troe, Combust. Flame,  158:594-601 (2011)
! Rate constant is for Ar
! Efficiencies for H2 and CO taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
""",
)

