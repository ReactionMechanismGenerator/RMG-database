#!/usr/bin/env python
# encoding: utf-8

name = "KlippensteinH2O2"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
H
1 H 1 0
""",
    reactant2 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    product1 = 
"""
O
1 O 2T 2
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (104000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15286, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n!<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>!\n!\n!                     ----- H2 Kinetic Mechanism -----\n!                     -----   Version 6-10-2011  -----\n!\n! (c) Burke, Chaos, Ju, Dryer, and Klippenstein; Princeton University, 2011.\n!\n!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!\n!  HOW TO USE THIS MECHANISM:\n!\n! (*) Due to limitations of CHEMKIN-II format (specifically, an inability to\n!     implement temperature-dependent collision efficiencies in falloff\n!     reactions) and the lack of fundamental understanding of the mixing rules\n!     for the falloff reactions with the bath gases that have different\n!     broadening factors, the present implementation represents a compromise\n!     (approximate) formulation.  As a consequence,\n!\n!     PRIOR TO ITS USE IN THE CALCULATIONS, THIS FILE HAS TO BE MODIFIED.\n!     DEPENDING ON WHAT BATH GAS (DILUTANT) IS MOST ABUNDANT IN YOUR SYSTEM\n!     (THE PRESENT CHOICES ARE N2, AR, OR HE),  YOU  SHOULD UNCOMMENT THE\n!     CORRESPONDING BLOCK FOR THE REACTION H+O2(+M)=HO2(+M), AND COMMENT THE\n!     BLOCK FOR OTHER DILUTANT(S).  AS GIVEN, THE MAIN DILUTANT IS SET TO BE N2.\n!\n!\n!  HOW TO REFERENCE THIS MECHANISM:\n!\n!     M.P. Burke, M. Chaos, Y. Ju, F.L. Dryer, S.J. Klippenstein\n!        "Comprehensive H2/O2 Kinetic Model for High-Pressure Combustion,"\n!        Int. J. Chem. Kinet. (2011).\n!\n!  FUTURE REVISIONS/UPDATES MAY BE FOUND ON THE FUELS AND COMBUSTION RESEARCH LABORATORY\n!  WEBSITE: < http://www.princeton.edu/mae/people/faculty/dryer/homepage/combustion_lab/ >\n!\n!\n!  HOW TO CONTACT THE AUTHORS:\n!\n!     Dr. Michael P. Burke\n!     R122 Building 200\n!     Chemical Sciences and Engineering Division\n!     Argonne National Laboratory\n!     Argonne, IL 60439\n!     Email: mpburke@anl.gov\n!\n!     Prof. Frederick L. Dryer\n!     D-329D Engineering Quadrangle\n!     Mechanical and Aerospace Engineering\n!     Princeton University\n!     Princeton, NJ 08544\n!     Phone: 609-258-5206\n!     Lab:   609-258-0316\n!     FAX:   609-258-1939\n!     Email: fldryer@princeton.edu\n!\n!\n!<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>!\n!\nELEMENTS\nH O N AR HE C\nEND\n!======================\n!H2-O2 Chain Reactions\n!======================\n! Hong et al., Proc. Comb. Inst. 33:309-316 (2011)',
    ),
    shortDesc = u"""""",
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
    reactant1 = 
"""
O
1 O 2T 2
""",
    reactant2 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3818000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7948, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (879200000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19170, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)
""",
)

entry(
    index = 4,
    reactant1 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H
1 H 1 0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Michael and Sutherland, J. Phys. Chem. 92:3853 (1988)
""",
)

entry(
    index = 5,
    reactant1 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
O
1 O 2T 2
""",
    product2 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33400, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-1930, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Baulch et al., J. Phys. Chem. Ref. Data, 21:411 (1992)
""",
)

entry(
    index = 6,
    reactant1 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product3 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.006e+26, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120180, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n!============================\n!H2-O2 Dissociation Reactions\n!============================\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)\nH2+AR = H+H+AR                                  5.840E+18 -1.10  1.0438E+05\nH2+HE = H+H+HE                                  5.840E+18 -1.10  1.0438E+05\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)\nO+O+AR = O2+AR                                  1.886E+13  0.00 -1.788E+03\nO+O+HE = O2+HE                                  1.886E+13  0.00 -1.788E+03\n! Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)',
    ),
    shortDesc = u"""""",
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
    reactant1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1 0
""",
    product1 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2750000.0, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (-1451, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n!=================================\n! Formation and consumption of HO2\n!=================================\n! High-pressure limit from Troe, Proc. Comb. Inst. 28:1463-1469 (2000)\n! Low-pressure  limit from Michael et al., J. Phys. Chem. A 106:5297-5313\n! Centering factors from Fernandes et al., Phys. Chem. Chem. Phys. 10:4313-4321 (2008)\n!=================================================================================\n! Michael et al., Proc. Comb. Inst. 28:1471 (2000)\n!HO2+H = H2+O2                                     3.659E+06  2.09 -1.451E+03\n!Scaled by 0.75',
    ),
    shortDesc = u"""""",
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
    reactant1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1 0
""",
    product1 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70790000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (295, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Mueller et al., Int. J. Chem. Kinetic. 31:113 (1999)
""",
)

entry(
    index = 9,
    reactant1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T 2
""",
    product1 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28500000000.0, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (-723.93, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)\n!HO2+O = O2+OH                                   4.750E+11  1.00 -7.2393E+02\n!Scaled by 0.60',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Fernandez-Ramos and Varandas, J. Phys. Chem. A 106:4077-4083 (2002)
!HO2+O = O2+OH                                   4.750E+11  1.00 -7.2393E+02
!Scaled by 0.60
""",
)

entry(
    index = 10,
    reactant1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Keyser, J. Phys. Chem. 92:1193 (1988)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Keyser, J. Phys. Chem. 92:1193 (1988)
""",
)

entry(
    index = 11,
    reactant1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (420000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11982, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (130000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1629.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n!=====================================\n!Formation and Consumption of H2O2\n!=====================================\n! Hippler et al., J. Chem. Phys. 93:1755 (1990)',
    ),
    shortDesc = u"""""",
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
    reactant1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1 0
""",
    product1 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 14,
    reactant1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1 0
""",
    product1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    reactant1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T 2
""",
    product1 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9550000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from KlippensteinH2O2.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    reactant1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1740000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (318, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (75900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7270, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Hong et al., J. Phys. Chem. A  114 (2010) 5718-5727',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Hong et al., J. Phys. Chem. A  114 (2010) 5718-5727
""",
)

entry(
    index = 18,
    reactant1 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
H
1 H 1 0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104380, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 19,
    reactant1 = 
"""
O
1 O 2T 2
""",
    reactant2 = 
"""
O
1 O 2T 2
""",
    product1 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6165000000000000.0, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 20,
    reactant1 = 
"""
O
1 O 2T 2
""",
    reactant2 = 
"""
H
1 H 1 0
""",
    product1 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Tsang and Hampson, J. Phys. Chem. Ref. Data, 15:1087 (1986)
""",
)

entry(
    index = 21,
    reactant1 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.064e+27, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120790, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 0.0, '[H][H]': 3.0, '[He]': 1.1, '[O][O]': 1.5, 'N#N': 2.0, '[C]=O': 1.9},
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)\n! Rate constant is for Ar with efficiencies from Michael et al., J. Phys. Chem. A, 106 (2002)',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Srinivasan and Michael, Int. J. Chem. Kinetic. 38 (2006)
! Rate constant is for Ar with efficiencies from Michael et al., J. Phys. Chem. A, 106 (2002)
""",
)

entry(
    index = 22,
    reactant1 = 
"""
H
1 H 1 0
""",
    reactant2 = 
"""
O2
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 2 {2,S} {3,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4650840000000.0, 'cm^3/(mol*s)'),
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
        efficiencies = {'O=C=O': 3.8, 'O': 14.0, '[H][H]': 2.0, '[He]': 0.8, '[O][O]': 0.78, '[C]=O': 1.9, '[Ar]': 0.67},
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n! Efficiencies for CO and CO2 taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)\n! MAIN BATH GAS IS N2 (comment this reaction otherwise)\n!',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
! Efficiencies for CO and CO2 taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)
! MAIN BATH GAS IS N2 (comment this reaction otherwise)
!
""",
)

entry(
    index = 23,
    reactant1 = 
"""
H2O2
1 O 0 2 {2,S} {3,S}
2 O 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    product1 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2000000000000.0, 's^-1'),
            n = 0.9,
            Ea = (48749, 'cal/mol'),
            T0 = (1, 'K'),
        ),
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
        comment = 'Reaction and kinetics from KlippensteinH2O2.\n!=================================================================================\n! MAIN BATH GAS IS AR OR HE (comment this reaction otherwise)\n!\n!H + O2 (+M) <=> HO2 (+M)      4.65084E+12  0.44  0.000E+00    0.0 0.0 0.0\n!H2/ 3.0/ H2O/ 21/ O2/ 1.1/ CO/ 2.7/ CO2/ 5.4/ HE/ 1.2/ N2/ 1.5/\n!=================================================================================\n! Troe, Combust. Flame,  158:594-601 (2011)\n! Rate constant is for Ar\n! Efficiencies for H2 and CO taken from Li et al., Int. J. Chem. Kinet. 36:566-575 (2004)',
    ),
    shortDesc = u"""""",
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

