#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/GlarborgH2S"
shortDesc = u""
longDesc = u"""
H2S oxidation at high pressures

An Exploratory Flow Reactor Study of H2S Oxidation at 30-100 Bar
Y. Song, H. Hashemi, J.M. Christensen, C. Zou, B.S. Haynes, P. Marshall, P. Glarborg
International Journal of Chemical Kinetics 49(1), 2017, 37-52
DOI: 10.1002/kin.21055
"""

entry(
    index = 1,
    label = "H2S <=> S + H2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.6e+24, 'cm^3/(mol*s)'),
            n = -2.613,
            Ea = (89100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
H Shiina A Miyoshi H Matsui J. Phys. Chem. A 1998, 102, 3556-3559
""",
)

entry(
    index = 2,
    label = "H2S + H <=> SH + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (904, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Peng JP Hu XH MArshall P JOURNAL OF PHYSICAL CHEMISTRY A  103 5307-5311 1999
""",
)

entry(
    index = 3,
    label = "H2S + O <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+07, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (2900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Goumri A Laakso D Rocha JDR Smith CE MArshall P J Chem Phys 102 161-169 1995
H2S+O=SH+OH 1.80E+05 2.6 2532.0 ! Wang et al. (2005)
""",
)

entry(
    index = 4,
    label = "H2S + O <=> HSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (5099, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Goumri A Laakso D Rocha JDR Smith CE MArshall P J Chem Phys 102 161-169 1995
""",
)

entry(
    index = 5,
    label = "H2S + OH <=> SH + H2O",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(8.7e+13, 'cm^3/(mol*s)'), n=-0.7, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.1e+07, 'cm^3/(mol*s)'),
                n = 1.77,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
)

entry(
    index = 6,
    label = "H2S + HO2 <=> HSO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1, 'cm^3/(mol*s)'),
        n = 3.288,
        Ea = (6224, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou (Molina Sendt TST) 2009
""",
)

entry(
    index = 7,
    label = "SH + H2O2 <=> H2S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56000, 'cm^3/(mol*s)'),
        n = 2.823,
        Ea = (8668, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 8,
    label = "SH + HO2 <=> H2S + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (38000, 'cm^3/(mol*s)'),
        n = 2.775,
        Ea = (-1529, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 9,
    label = "H2S + O2 <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 10,
    label = "H2S + O3 <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1700, 'cm^3/(mol*s)'), n=2.67, Ea=(11390, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(13000, 'cm^3/(mol*s)'), n=2.19, Ea=(11607, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5.3e+08, 'cm^3/(mol*s)'),
                n = 1.66,
                Ea = (11655, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'MOUHEM13',
            ),
        ],
    ),
)

entry(
    index = 11,
    label = "H2S + O3 <=> HOSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (11369, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
MOUHEM13
""",
)

entry(
    index = 12,
    label = "H2S + S <=> SH + SH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(7.4e+06, 'cm^3/(mol*s)'), n=2.3, Ea=(9000, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.7e+07, 'cm^3/(mol*s)'),
                n = 1.325,
                Ea = (-436, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'kinf (fitted from figure) ##\nH2S+S=SH+SH   1.2E18 -1.685     5970 !\nY Gao CR Zhou K Sendt BS Haynes P MArshall Proc Combust Inst 33 (2011) 459-465',
            ),
        ],
    ),
)

entry(
    index = 13,
    label = "HSO + SH <=> SO + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
H2S+SO=HSO+SH                        5.4E03  3.209    26824 !
Zhou TST (2009) rv too fast
""",
)

entry(
    index = 14,
    label = "H2S + SO <=> HOS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

#entry(
#    index = 15,
#    label = "H2S + SO(S) <=> HSO + SH",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (11000, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc = 
#u"""
#Zhou est (2009)
#""",
#)

entry(
    index = 16,
    label = "H2S + SO2 <=> S2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+06, 'cm^3/(mol*s)'),
        n = 1.857,
        Ea = (37810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 17,
    label = "H2S + SO2 <=> H2S2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.5e+18, 'cm^3/(mol*s)'),
        n = -2.121,
        Ea = (33530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS JPCA 109 8180-8186 2005
""",
)

entry(
    index = 18,
    label = "H2S + HSO <=> SH + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 19,
    label = "H2S + HOS <=> SH + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 20,
    label = "H2S + S2O <=> H2S3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.307,
        Ea = (30450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 21,
    label = "H2S + S2O <=> S3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+07, 'cm^3/(mol*s)'),
        n = 1.506,
        Ea = (34010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 22,
    label = "H2S + S2O <=> HSSSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9, 'cm^3/(mol*s)'),
        n = 3.638,
        Ea = (22681, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 23,
    label = "S + H <=> SH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PROC COMBUST INST 29 2439-2446 2002 est
""",
)

entry(
    index = 24,
    label = "S + H2 <=> SH + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
H Shiina A Miyoshi H Matsui J. Phys. Chem. A 1998, 102, 3556-3559
""",
)

entry(
    index = 25,
    label = "SH + O <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+11, 'cm^3/(mol*s)'),
        n = 0.724,
        Ea = (-1027, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS PROC COMBUST INST 31 257-265 2007
""",
)

entry(
    index = 26,
    label = "SH + O <=> S + OH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (4.3e+06, 'cm^3/(mol*s)'),
                n = 2.103,
                Ea = (3583, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Sendt K Haynes BS PROC COMBUST INST 31 257-265 2007',
            ),
        ],
    ),
)

entry(
    index = 27,
    label = "SH + OH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
pw est (Tsuchiya data; Goumri et al.)
SH+OH=S+H2O                          1.7E05  2.465    -1637 !
Zhou TST (2009)
""",
)

entry(
    index = 28,
    label = "SH + OH <=> HOS + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est
""",
)

entry(
    index = 29,
    label = "SH + HO2 <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+08, 'cm^3/(mol*s)'),
        n = 1.477,
        Ea = (-2169, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 30,
    label = "SH + HO2 <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (320, 'cm^3/(mol*s)'),
        n = 2.579,
        Ea = (-2071, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou (Molina Sendt TST) (2009)
""",
)

entry(
    index = 31,
    label = "S + H2O2 <=> SH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (12619, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 32,
    label = "SH + O2 <=> HSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3e+06, 'cm^3/(mol*s)'),
        n = 1.816,
        Ea = (20008, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 113, 2975-2981
""",
)

entry(
    index = 33,
    label = "SH + O2 <=> S + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+06, 'cm^3/(mol*s)'),
        n = 2.017,
        Ea = (36913, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 113, 2975-2981
""",
)

entry(
    index = 34,
    label = "SH + O2 <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (75000, 'cm^3/(mol*s)'),
        n = 2.052,
        Ea = (16384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 113, 2975-2981
""",
)

entry(
    index = 35,
    label = "SH + O2 <=> H + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000, 'cm^3/(mol*s)'),
        n = 2.123,
        Ea = (11020, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
pw (PM 1606)
SH+O2=H+SO2                          6.5E11  0.000    15000 !
J.D. GArrido, M.Y. Ballester, Y. Orozco-Gonzalez, S. Canuto, J. Phys. Chem. A 2011, 115, 1453-1461.
""",
)

entry(
    index = 36,
    label = "SH + H2O2 <=> HSOH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (9829, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 37,
    label = "SH + O3 <=> HSO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (556, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04
""",
)

entry(
    index = 38,
    label = "SH + S <=> S2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+12, 'cm^3/(mol*s)'),
        n = 0.543,
        Ea = (-29, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou QRRK (2009)
""",
)

entry(
    index = 39,
    label = "SH + SO <=> HSO + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 40,
    label = "SH + SO <=> HOS + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 41,
    label = "SH + HSO <=> S + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 42,
    label = "SH + HSO <=> S2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 43,
    label = "S2O + H2 <=> SH + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 44,
    label = "SH + SO <=> S2O + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 45,
    label = "SH + SO2 <=> HSO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 46,
    label = "SH + SO2 <=> HOS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 47,
    label = "SH + SO2 <=> OH + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 48,
    label = "SH + SO2 <=> HSSO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (33000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 49,
    label = "S + OH <=> H + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13, 'cm^3/(mol*s)'),
        n = 0.191,
        Ea = (-1361, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS Proc Combust Inst 2007, 31, 257-265
""",
)

entry(
    index = 50,
    label = "S + HO2 <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Ballester MY VArandas, AJC IJCK 40 533-540 2008
""",
)

entry(
    index = 51,
    label = "S + HO2 <=> HOS + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 52,
    label = "S + O2 <=> SO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (-1450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Lu C-W Wu Y-J Lee Y-P Zhu RS Lin MC J Chem Phys 2004, 121, 8271.
""",
)

entry(
    index = 53,
    label = "S + O3 <=> SO + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Atkinson R Baulch DL Cox RA Crowley JN Hampson RF Hynes RG Jenkin ME Rossi MJ Troe J Atmos Chem Phys 2004 4 1461-1738.
""",
)

entry(
    index = 54,
    label = "S + H2O2 <=> HOS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 55,
    label = "SO <=> S + O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4e+14, 'cm^3/(mol*s)'), n=0, Ea=(107000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Plach, H. J.; Troe, J. Int J Chem Kinet 1984, 16, 1531
""",
)

entry(
    index = 56,
    label = "SO + H <=> HSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+20, 'cm^6/(mol^2*s)'),
            n = -1.31,
            Ea = (662, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
""",
)

entry(
    index = 57,
    label = "SO + O <=> SO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.1e+22, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
Lu C-W Wu Y-J Lee Y-P Zhu RS Lin MC J Phys Chem A 2003, 107, 11020-11029
""",
)

entry(
    index = 58,
    label = "SO + HO2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
pw bArrierless
""",
)

entry(
    index = 59,
    label = "SO + O2 <=> SO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7600, 'cm^3/(mol*s)'),
        n = 2.37,
        Ea = (2970, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ALZ/GLA01 TSU/MAT97
SO+O2=SO2+O                          8.9E06  1.400     3712 ! GArland (1998)
""",
)

entry(
    index = 60,
    label = "SO + O3 <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2325, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Atkinson R Baulch DL Cox RA Crowley JN Hampson RF Hynes RG Jenkin ME Rossi MJ Troe J Atmos Chem Phys 2004 4 1461-1738.
""",
)

entry(
    index = 61,
    label = "SO + S <=> S2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.1e+22, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1.5},
    ),
    longDesc = 
u"""
est as SO+O+M
""",
)

entry(
    index = 62,
    label = "SO + SH <=> S2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
est
Zhou est (2009)
""",
)

#entry(
#    index = 63,
#    label = "SO(S) <=> SO",
#    degeneracy = 1,
#    kinetics = ThirdBody(
#        arrheniusLow = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
#        efficiencies = {},
#    ),
#    longDesc = 
#u"""
#Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
#""",
#)

#entry(
#    index = 64,
#    label = "SO(S) + O2 <=> SO2 + O",
#    degeneracy = 1,
#    kinetics = Arrhenius(
#        A = (1e+13, 'cm^3/(mol*s)'),
#        n = 0,
#        Ea = (0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    longDesc = 
#u"""
#Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
#""",
#)

entry(
    index = 65,
    label = "SO2 + H <=> SO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+21, 'cm^3/(mol*s)'),
        n = -2.22,
        Ea = (30736, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Hughes KJ Blitz MA Pilling MJ Robertson SH Proc Combust Inst 2002, 29, 2431-2437
""",
)

entry(
    index = 66,
    label = "SO2 + H <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.3e+08, 'cm^3/(mol*s)'),
            n = 1.59,
            Ea = (2470, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+31, 'cm^6/(mol^2*s)'),
            n = -5.19,
            Ea = (4510, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.39,
        T3 = (167, 'K'),
        T1 = (2191, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
MA Blitz KJ Hughes M Pillling SH Robertson J. Phys. Chem. A 110 (2006) 2996-3009
""",
)

entry(
    index = 67,
    label = "SO2 + H <=> HOSO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.4e+08, 'cm^3/(mol*s)'),
            n = 1.63,
            Ea = (7340, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.8e+37, 'cm^6/(mol^2*s)'),
            n = -6.14,
            Ea = (11070, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.283,
        T3 = (272, 'K'),
        T1 = (3995, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
MA Blitz KJ Hughes M Pillling SH Robertson J. Phys. Chem. A 110 (2006) 2996-3009
""",
)

entry(
    index = 68,
    label = "SO2 + O <=> SO3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.9e+27, 'cm^6/(mol^2*s)'),
            n = -3.58,
            Ea = (5206, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (371, 'K'),
        T1 = (7442, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
N2
A Yilmaz L HindiyArti AD Jensen P GlArborg P MArshall J. Phys. Chem. A 110 (2006) 6654-6659.
""",
)

entry(
    index = 69,
    label = "SO2 + OH <=> HOSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.7e+12, 'cm^3/(mol*s)'), n=-0.27, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+27, 'cm^6/(mol^2*s)'),
            n = -4.09,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.1,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=S=O': 5, 'O': 5, 'N#N': 1},
    ),
    longDesc = 
u"""
MA Blitz KJ Hughes MJ Pilling J Phys Chem A 107 (2003) 1971-1978
""",
)

entry(
    index = 70,
    label = "SO2 + H2O <=> VDW1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 71,
    label = "SO2 + O3 <=> SO3 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
JPL 02 upper limit Zhou (2009)
""",
)

entry(
    index = 72,
    label = "SO2 + CO <=> SO + CO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (65900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
GB Bacskay JC Mackie J. Phys. Chem. A 109 (2005) 2019-2025
""",
)

entry(
    index = 73,
    label = "SO2 + S <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e-16, 'cm^3/(mol*s)'),
        n = 8.21,
        Ea = (9600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Y Murakami S Onishi T Kobayashi N Fujii N Isshiki K Tsuchiya A Tezaki H Matsui J Phys Chem A 107 2003 10996-11000
""",
)

entry(
    index = 74,
    label = "SO2 + SO2 <=> SO3 + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (75000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
L HindiyArti P GlArborg P MArshall J. Phys. Chem. A 111 (2007) 3984-3991
""",
)

entry(
    index = 75,
    label = "SO3 + H <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+09, 'cm^3/(mol*s)'),
        n = 1.22,
        Ea = (3320, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
L HindiyArti P GlArborg P MArshall J. Phys. Chem. A 111 (2007) 3984-3991
""",
)

entry(
    index = 76,
    label = "SO3 + H <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (250000, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (50300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 77,
    label = "SO3 + O <=> SO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (29200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
L HindiyArti P GlArborg P MArshall J. Phys. Chem. A 111 (2007) 3984-3991
""",
)

entry(
    index = 78,
    label = "SO3 + OH <=> SO2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48000, 'cm^3/(mol*s)'),
        n = 2.46,
        Ea = (27250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
L HindiyArti P GlArborg P MArshall J. Phys. Chem. A 111 (2007) 3984-3991
""",
)

entry(
    index = 79,
    label = "SO3 + S <=> SO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 80,
    label = "HSO + H <=> SO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347 est
""",
)

entry(
    index = 81,
    label = "HSO + H <=> HOS + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 82,
    label = "HSO + H <=> HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+20, 'cm^3/(mol*s)'),
        n = -3.14,
        Ea = (920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 83,
    label = "HSO + H <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (1560, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 84,
    label = "HSO + H <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+09, 'cm^3/(mol*s)'),
        n = 1.37,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 85,
    label = "HSO + H <=> H2SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+17, 'cm^3/(mol*s)'),
        n = -2.47,
        Ea = (50, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 86,
    label = "HSO + O <=> HSO2",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.1e+19, 'cm^6/(mol^2*s)'),
            n = -1.73,
            Ea = (-50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 87,
    label = "HSO + O <=> SO2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.5e+14, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 88,
    label = "HSO + O <=> HOSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.9e+19, 'cm^6/(mol^2*s)'),
            n = -1.61,
            Ea = (1590, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 89,
    label = "HSO + O <=> HOS + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (5340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 90,
    label = "HSO + O <=> OH + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 91,
    label = "HSO + OH <=> HOSHO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.2e+28, 'cm^3/(mol*s)'),
        n = -5.44,
        Ea = (3170, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 92,
    label = "HSO + OH <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+07, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (3750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 93,
    label = "HSO + OH <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (470, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 94,
    label = "HSO + OH <=> H2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 95,
    label = "HSO + HO2 <=> SO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 96,
    label = "HSO + O2 <=> SO + HO2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (640000, 'cm^3/(mol*s)'),
                n = 2.627,
                Ea = (19013, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Zhou TST (2009) (quArtet TS); Ea-2.5 kcal/mol (pw)',
            ),
            Arrhenius(
                A = (29, 'cm^3/(mol*s)'),
                n = 3.2,
                Ea = (14529, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'pw (PM 2015) (doublet TS)',
            ),
        ],
    ),
)

entry(
    index = 97,
    label = "HSO + O2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37, 'cm^3/(mol*s)'),
        n = 2.764,
        Ea = (6575, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 98,
    label = "HSO + O2 <=> HSO2 + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e-07, 'cm^3/(mol*s)'),
        n = 5.1,
        Ea = (11312, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
""",
)

entry(
    index = 99,
    label = "HSO + O3 <=> SH + O2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04, LEEWAN94
""",
)

entry(
    index = 100,
    label = "HSO + O3 <=> HSO2 + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
ATKTRO04, LEEWAN94
""",
)

entry(
    index = 101,
    label = "HSO + O3 <=> SO + OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5, 'cm^3/(mol*s)'),
        n = 3.63,
        Ea = (7191, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
pw (PM 151027)
""",
)

entry(
    index = 102,
    label = "HSO + HSO <=> SO + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 103,
    label = "HSO + S2 <=> HSS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 104,
    label = "H + SO <=> HOS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.6e+20, 'cm^6/(mol^2*s)'),
            n = -1.924,
            Ea = (-29, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'N#N': 0},
    ),
)

entry(
    index = 105,
    label = "H + SO + N2 <=> HOS + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+21, 'cm^6/(mol^2*s)'),
        n = -2.093,
        Ea = (-72, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS Proc Combust Inst 2007, 31, 257-265
""",
)

entry(
    index = 106,
    label = "HOS <=> HSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5.8e+11, 'cm^3/(mol*s)'), n=0, Ea=(32722, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'N#N': 0},
    ),
)

entry(
    index = 107,
    label = "HOS + N2 <=> HSO + N2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24601, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS Proc Combust Inst 2007, 31, 257-265
""",
)

entry(
    index = 108,
    label = "HOS + H <=> H2 + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 109,
    label = "HOS + O <=> OH + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 110,
    label = "HOS + O <=> H + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 111,
    label = "HOS + OH <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 112,
    label = "HOS + OH <=> H2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 113,
    label = "HOS + O2 <=> HO2 + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (640000, 'cm^3/(mol*s)'),
        n = 2.627,
        Ea = (19013, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 114,
    label = "HOS + O2 <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (37, 'cm^3/(mol*s)'),
        n = 2.764,
        Ea = (6575, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 115,
    label = "HOS + HO2 <=> SO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 116,
    label = "HOS + HOS <=> SO + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 117,
    label = "HOS + S2 <=> HSS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 118,
    label = "HOS + S2 <=> S3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 119,
    label = "HSOH <=> SH + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+39, 's^-1'),
        n = -8.75,
        Ea = (75200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 120,
    label = "HSOH <=> S + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+29, 's^-1'),
        n = -5.6,
        Ea = (54500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 121,
    label = "HSOH <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+16, 's^-1'),
        n = -3.4,
        Ea = (86500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 122,
    label = "HSOH + HO2 <=> HSO + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 123,
    label = "HSOH + HO2 <=> HOS + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 124,
    label = "HSOH + O2 <=> HSO + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 125,
    label = "HSOH + O2 <=> HOS + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 126,
    label = "HSOH + O <=> HSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 127,
    label = "HSOH + O <=> HOS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 128,
    label = "HSOH + H <=> HSO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 129,
    label = "HSOH + H <=> HOS + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 130,
    label = "HSOH + OH <=> HSO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 131,
    label = "HSOH + OH <=> HOS + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 132,
    label = "HOSO <=> OH + SO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.9e+21, 's^-1'), n=-2.54, Ea=(75891, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.2e+46, 'cm^3/(mol*s)'),
            n = -9.02,
            Ea = (52953, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.95,
        T3 = (2989, 'K'),
        T1 = (1.1, 'K'),
        efficiencies = {},
    ),
    longDesc = 
u"""
Hughes KJ Blitz MA Pilling MJ Robertson SH Proc Combust Inst 2002, 29, 2431-2437
""",
)

entry(
    index = 133,
    label = "HOSO <=> HSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+09, 's^-1'), n=1.03, Ea=(50000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.7e+35, 'cm^3/(mol*s)'),
            n = -5.64,
            Ea = (55400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.4,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
A Goumri J-DR Rocha D Laakso CE Smith P MArshall J. Phys. Chem. A 103 (1999) 11328-11335
""",
)

entry(
    index = 134,
    label = "HOSO <=> O + HOS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.5e+30, 'cm^3/(mol*s)'),
            n = -4.8,
            Ea = (119000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 135,
    label = "HOSO + H <=> SO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+07, 'cm^3/(mol*s)'),
        n = 1.72,
        Ea = (-1286, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
X Hu P MArshall, poster presented at the 18th International Symposium on Gas Kinetics, Bristol, UK, August, 7-12, 2004
""",
)

entry(
    index = 136,
    label = "HOSO + H <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
X Hu P MArshall, poster presented at the 18th International Symposium on Gas Kinetics, Bristol, UK, August, 7-12, 2004
Original reaction was HOSO + H <=> SO(S) + H2O
""",
)

entry(
    index = 137,
    label = "HOSO + O <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 138,
    label = "HOSO + OH <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347 est
""",
)

entry(
    index = 139,
    label = "HOSO + HO2 <=> SO2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 140,
    label = "HOSO + O2 <=> HO2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96, 'cm^3/(mol*s)'),
        n = 2.355,
        Ea = (-10130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
(T>400K)
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
""",
)

entry(
    index = 141,
    label = "HOSO + SH <=> SO2 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 142,
    label = "HOSO + S <=> SO2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 143,
    label = "HOSO + SO <=> SO2 + HSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 144,
    label = "HOSO + SO <=> SO2 + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 145,
    label = "HOSO + HSO <=> SO2 + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 146,
    label = "HOSO + HOS <=> SO2 + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 147,
    label = "HOSO + HSS <=> SO2 + HSSH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 148,
    label = "HOSO + S2 <=> SO2 + HSS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 149,
    label = "HSO2 + H <=> SO2 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0.46,
        Ea = (-262, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
X Hu P MArshall, poster presented at the 18th International Symposium on Gas Kinetics, Bristol, UK, August, 7-12, 2004
""",
)

entry(
    index = 150,
    label = "HSO2 + O <=> SO2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 151,
    label = "HSO2 + OH <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 152,
    label = "HSO2 + HO2 <=> SO2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 153,
    label = "HSO2 + O2 <=> HO2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (-235, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Rasmussen CL GlArborg P MArshall P Proc Combust Inst 2007, 31, 339-347
""",
)

entry(
    index = 154,
    label = "HSO2 + O3 <=> SO2 + OH + O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
est
""",
)

entry(
    index = 155,
    label = "HSO2 + SH <=> SO2 + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 156,
    label = "HSO2 + S <=> SO2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 157,
    label = "HSO2 + SO <=> SO2 + HSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 158,
    label = "HSO2 + SO <=> SO2 + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 159,
    label = "HSO2 + HSO <=> SO2 + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 160,
    label = "HSO2 + HSS <=> SO2 + HSSH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 161,
    label = "HSO2 + S2 <=> SO2 + HSS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 162,
    label = "SH + O2 <=> HSOO",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (8.7e+14, 'cm^3/(mol*s)'),
            n = -0.26,
            Ea = (298, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.1e+19, 'cm^6/(mol^2*s)'),
            n = -2.01,
            Ea = (20, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
A. Goumri, J.-D.R. Rocha, D. Laakso, C.E. Smith, P. MArshall, J. Phys. Chem. A 1999, 103, 11328-11335.
""",
)

entry(
    index = 163,
    label = "HSOO <=> HSO + O",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(2e+19, 's^-1'), n=-1.07, Ea=(28374, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.3e+34, 'cm^3/(mol*s)'),
            n = -5.87,
            Ea = (30957, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
A. Goumri, J.-D.R. Rocha, D. Laakso, C.E. Smith, P. MArshall, J. Phys. Chem. A 1999, 103, 11328-11335.
""",
)

entry(
    index = 164,
    label = "H2SO <=> H2S + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.9e+28, 's^-1'),
        n = -6.66,
        Ea = (71700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 165,
    label = "HOSHO <=> HOSO + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.4e+30, 's^-1'),
        n = -5.89,
        Ea = (73800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 166,
    label = "HOSHO <=> SO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+24, 's^-1'),
        n = -3.59,
        Ea = (59500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 167,
    label = "HOSHO + H <=> HOSO + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 168,
    label = "HOSHO + O <=> HOSO + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 169,
    label = "HOSHO + OH <=> HOSO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 170,
    label = "HOSO2 <=> HOSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+18, 's^-1'),
        n = -2.34,
        Ea = (106300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 171,
    label = "HOSO2 <=> SO3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+18, 's^-1'),
        n = -2.91,
        Ea = (54900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 172,
    label = "HOSO2 + H <=> SO2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 173,
    label = "HOSO2 + O <=> SO3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 174,
    label = "HOSO2 + OH <=> SO3 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
P GlArborg D Kubel K Dam-Johansen H-M Chiang JW Bozzelli Int J Chem Kinet 28 (1996) 773-790
""",
)

entry(
    index = 175,
    label = "HOSO2 + O2 <=> HO2 + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (656, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Atkinson R Baulch DL Cox RA Crowley JN Hampson RF Hynes RG Jenkin ME Rossi MJ Troe J Atmos Chem Phys 2004 4 1461-1738.!
""",
)

entry(
    index = 176,
    label = "HOSO2 + S <=> SH + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 177,
    label = "SH + SH <=> HSSH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (9e+11, 'cm^3/(mol*s)'),
            n = 0.155,
            Ea = (-1432, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.329e+31, 'cm^6/(mol^2*s)'),
            n = -4.943,
            Ea = (1998, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (254, 'K'),
        T1 = (2373, 'K'),
        efficiencies = {},
    ),
    longDesc = 
u"""
A-factor reduced
CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 112, 3239-3247
""",
)

entry(
    index = 178,
    label = "H2S + S <=> HSSH",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.4e+07, 'cm^3/(mol*s)'),
            n = 1.28,
            Ea = (-478, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.4e+21, 'cm^6/(mol^2*s)'),
            n = -1.612,
            Ea = (1670, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (726, 'K'),
        T1 = (726, 'K'),
        efficiencies = {'N#N': 1.3},
    ),
    longDesc = 
u"""
CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 112, 3239-3247
""",
)

entry(
    index = 179,
    label = "HSSH + H <=> HSS + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+07, 'cm^3/(mol*s)'),
        n = 1.933,
        Ea = (-1408, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446  2002
""",
)

entry(
    index = 180,
    label = "HSSH + H <=> H2S + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+08, 'cm^3/(mol*s)'),
        n = 1.724,
        Ea = (467, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 181,
    label = "HSSH + O <=> HSS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 182,
    label = "HSSH + O <=> HSO + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 183,
    label = "HSSH + OH <=> HSS + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 184,
    label = "HSSH + HO2 <=> HSS + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 185,
    label = "HSSH + O2 <=> HSS + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 186,
    label = "HSSH + S <=> HSS + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+06, 'cm^3/(mol*s)'),
        n = 2.31,
        Ea = (1204, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 187,
    label = "HSSH + SH <=> HSS + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6400, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (-1480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 188,
    label = "HSSH + SO <=> HSS + HSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 189,
    label = "HSSH + SO <=> HSS + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 190,
    label = "HSSH + HSO <=> HSS + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 191,
    label = "HSSH + HOS <=> HSS + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 192,
    label = "S2 + H <=> HSS",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.2e+25, 'cm^6/(mol^2*s)'),
            n = -2.84,
            Ea = (1665, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'S': 1.1, '[Ar]': 0.88},
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 193,
    label = "HSS + H <=> SH + SH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (9.7e+07, 'cm^3/(mol*s)'),
                n = 1.62,
                Ea = (-1030, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.6e+18, 'cm^3/(mol*s)'),
                n = -0.983,
                Ea = (261, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002\nCR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 112, 3239-3247',
            ),
        ],
    ),
)

entry(
    index = 194,
    label = "HSS + H <=> H2 + S2",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+08, 'cm^3/(mol*s)'), n=1.75, Ea=(-877, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (2.9e+16, 'cm^3/(mol*s)'),
                n = -0.894,
                Ea = (-56, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 112, 3239-3247',
            ),
        ],
    ),
)

entry(
    index = 195,
    label = "HSS + H <=> H2S + S",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1.5e+08, 'cm^3/(mol*s)'),
                n = 1.551,
                Ea = (2259, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (4.2e+18, 'cm^3/(mol*s)'),
                n = -1.563,
                Ea = (472, 'cal/mol'),
                T0 = (1, 'K'),
                comment = 'CR Zhou K Sendt BS Haynes J. Phys. Chem. A 2009, 112, 3239-3247',
            ),
        ],
    ),
)

entry(
    index = 196,
    label = "HSS + O <=> S2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 197,
    label = "HSS + O <=> SH + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 198,
    label = "HSS + OH <=> S2 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 199,
    label = "HSS + HO2 <=> S2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 200,
    label = "HSS + O2 <=> HSSO + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 201,
    label = "HSS + O2 <=> S2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84, 'cm^3/(mol*s)'),
        n = 2.95,
        Ea = (7071, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
pw (PM 2015)
""",
)

entry(
    index = 202,
    label = "HSS + O2 <=> HSO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6600, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7071, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou (Molina Sendt TST) (2009)
""",
)

entry(
    index = 203,
    label = "HSS + S <=> S2 + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+06, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (-600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 204,
    label = "HSS + SH <=> H2S + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6300, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (-1105, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 205,
    label = "HSS + SO <=> S3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 206,
    label = "HSS + SO3 <=> HSSO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 207,
    label = "HSS + HSO <=> HSSO + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 208,
    label = "HSS + HSO <=> S2 + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 209,
    label = "HSS + HOS <=> S2 + HSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 210,
    label = "HSS + HSS <=> HSSH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (-1672, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Jazbec M Haynes BS PCI 29:2439-2446 2002
""",
)

entry(
    index = 211,
    label = "S + S <=> S2",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.4e+10, 'cm^3/(mol*s)'), n=0, Ea=(-825, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(7.2e+14, 'cm^6/(mol^2*s)'), n=0, Ea=(-408, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Du, S.Y.; Francisco, J.S.; Shepler, B.C.; Peterson, K.A. J. Chem. Phys. 128 204306 2008
""",
)

entry(
    index = 212,
    label = "S2 + O <=> S2O",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.9e+21, 'cm^6/(mol^2*s)'), n=-2.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou (2009) est O+O+M
""",
)

entry(
    index = 213,
    label = "S2 + O <=> SO + S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (-231, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
Singleton DL Cvetanovic RJ JPCRD 17:1377 1988  7.0E12 0 0
""",
)

entry(
    index = 214,
    label = "S2 + O2 <=> S2O + O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000, 'cm^3/(mol*s)'),
        n = 2.539,
        Ea = (34376, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 215,
    label = "S2 + O2 <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.3003, 'cm^3/(mol*s)'),
        n = 2.453,
        Ea = (30440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 216,
    label = "S2 + S <=> S3",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 217,
    label = "S2 + S2 <=> S4",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 218,
    label = "S2O + H <=> HSSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.4e+22, 'cm^6/(mol^2*s)'),
            n = -2.591,
            Ea = (287, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou (2009) est HSO+M
""",
)

entry(
    index = 219,
    label = "S2O + H <=> OH + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 220,
    label = "S2O + O <=> SO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Singleton DL Cvetanovic RJ JPCRD 17:1377 1988
S2O+OH=S2+HO2                        1.0E13   0.000   40000 !
Zhou est (2009)
""",
)

entry(
    index = 221,
    label = "S2O + S <=> SO + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 222,
    label = "S2O + SH <=> HSO + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 223,
    label = "S2O + SH <=> HSS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 224,
    label = "S2O + SH <=> S3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (21450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 225,
    label = "S2O + SO2 <=> S2 + SO3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 226,
    label = "S2O + HSO2 <=> HSSO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (32000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
S2O+S2=S3+SO                         1.0E14   0.000   18000 !
Zhou est (2009)
""",
)

entry(
    index = 227,
    label = "S2O + S2O <=> S3 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 228,
    label = "HSSO + H <=> S2O + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 229,
    label = "HSSO + H <=> HSS + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 230,
    label = "HSSO + O <=> S2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 231,
    label = "HSSO + O <=> SH + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 232,
    label = "HSSO + OH <=> S2O + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 233,
    label = "HSSO + OH <=> HSS + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (27000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 234,
    label = "HSSO + HO2 <=> S2O + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 235,
    label = "HSSO + S <=> HSS + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 236,
    label = "HSSO + S <=> S2O + SH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 237,
    label = "HSSO + SH <=> S2O + H2S",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 238,
    label = "HSSO + HSS <=> S2O + HSSH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 239,
    label = "HSSO + S2 <=> S2O + HSS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 240,
    label = "SO2 + S <=> SSO2",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.7e+12, 'cm^3/(mol*s)'), n=0, Ea=(1689, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.9e+28, 'cm^6/(mol^2*s)'),
            n = -3.58,
            Ea = (5206, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.43,
        T3 = (371, 'K'),
        T1 = (7442, 'K'),
        efficiencies = {'O=S=O': 10, 'O': 10, 'N#N': 1},
    ),
    longDesc = 
u"""
est 10 x SO2+O+M
SSO2+M=S+SO2+M                       1.0E15   0.000   30000 !
Zhou est (2009)
""",
)

entry(
    index = 241,
    label = "SSO2 + H <=> SH + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
est pw
""",
)

entry(
    index = 242,
    label = "SSO2 + O <=> SO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
est pw
""",
)

entry(
    index = 243,
    label = "SSO2 + OH <=> HOS + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
est pw
""",
)

entry(
    index = 244,
    label = "SSO2 + S <=> S2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 245,
    label = "SO + SO <=> OSSO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.2e+32, 'cm^6/(mol^2*s)'),
            n = -5.75,
            Ea = (3044, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou TST (2009)
""",
)

entry(
    index = 246,
    label = "OSSO + H <=> OH + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 247,
    label = "OSSO + H <=> SO + HSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 248,
    label = "OSSO + H <=> SO + HOS",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 249,
    label = "OSSO + H <=> HO2 + S2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 250,
    label = "OSSO + O <=> SO + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 251,
    label = "OSSO + O <=> O2 + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 252,
    label = "OSSO + OH <=> HO2 + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 253,
    label = "OSSO + OH <=> HOSO + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 254,
    label = "OSSO + SO <=> SO2 + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 255,
    label = "OSSO + S <=> S2O + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 256,
    label = "OSSO + S <=> S2 + SO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 257,
    label = "OSSO + SH <=> HSO + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 258,
    label = "OSSO + S2 <=> S2O + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 259,
    label = "HSSO2 <=> SH + SO2",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 260,
    label = "HSSO2 <=> S2O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (33700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 261,
    label = "H2S2O2 + H2O <=> H2S + VDW1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (390000, 'cm^3/(mol*s)'),
        n = 1.66,
        Ea = (3740, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 262,
    label = "H2S2O2 + H2O <=> H2O + H2O + S2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (360000, 'cm^3/(mol*s)'),
        n = 1.562,
        Ea = (14290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 263,
    label = "H2S2O2 + SH <=> HSSH + HOSO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Sendt K Haynes BS J PHYS CHEM A 109 8180-8186 2005
""",
)

entry(
    index = 264,
    label = "S3 + H2O <=> HSSSOH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (25000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 265,
    label = "S3 + S2 <=> S5",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 266,
    label = "S3 + S3 <=> S6",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 267,
    label = "S3 + S2O <=> S4 + SO",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 268,
    label = "S3 + S4 <=> S7",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

entry(
    index = 269,
    label = "S4 + S4 <=> S8",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.9e+15, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    longDesc = 
u"""
Zhou est (2009)
""",
)

