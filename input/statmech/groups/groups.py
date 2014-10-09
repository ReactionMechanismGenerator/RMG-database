#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Values"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = -1,
    label = "R!H",
    group = "OR{R!Hx0, R!Hx1, R!Hx2, R!Hx3}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx0",
    group = 
"""
1 * R!H 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx1",
    group = 
"""
1 * R!H 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx2",
    group = 
"""
1 * R!H {2S,2T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx3",
    group = 
"""
1 * R!H {3D,3Q}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R0",
    group = 
"""
1 * C 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 1,
    label = "RsCH3",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H X {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2750, 2850, 3), 	#C-H stretch
            (1350, 1500, 2), 	#R-C-H bend
            (700, 800, 1),		#R-C-H rock
            (1000, 1100, 1),	#R-C-H rock
            (1350, 1400, 1),	#Umbrella
            (900, 1100, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = u"""Alkane end group""",
    longDesc = 
u"""
Goldsmith. (2010). Predicting Combustion Properties of Hydrocarbon Fuel Mixtures. (Doctoral dissertation). 
pg 125 Retrieved from http://web.mit.edu/cfgold/www/Homepage/Thesis_files/Thesis.pdf
""",
)

entry(
    index = 2,
    label = "RdCH2",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H X {1,D}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2950, 3100, 2),	#C-H stretch
            (1330, 1430, 1),	#R-C-H scissor
            (900, 1050, 1),		#R-C-H swing
            (1000, 1050, 1),	#R-C-H rock
            (1600, 1700, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""Alkene end group""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CtCH",
    group =
"""
1 * C 0 {2,T} {3,S}
2   C X	{1,T}
3   H 0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (750, 770, 2),		#R-C-H bend
            (3350, 3450, 1),	#C-H stretch
            (2000, 2200, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""Alkyne end group""",
    longDesc = 
u"""


""",
)

entry(
    index = 4,
    label = "RsCH2sR",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H X {1,S}
3   R!H X {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2750, 2850, 2),	#C-H stretch
            (1425, 1450, 1),	#H-C-H scissor
            (1225, 1275, 1),	#R-C-H symmetric
            (1270, 1340, 1),	#R-C-H asymmetric
            (700, 800, 1),		#H-C-H side rock
            (300, 400, 1),		#R-C-R scissor
        ],
        symmetry = 4,
    ),
    shortDesc = u"""separated carbon with two single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 6,
    label = "Aldehyde",
    group =
"""
1 * C	0	{2,D} {3,S} {4,S}
2   O	0	{1,D}
3   R!H	X 	{1,S}
4   H   0	{1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2695, 2870, 1),	#C-H stretch
            (700, 800, 1),		#R-C-H bend
            (1380, 1410, 1), 	#R-C-H bend
            (450, 500, 1),		#OdC-R scissor
            (1750, 1800, 1),	#OdC stretch
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon with double bond to oxygen and single bond to R""",
    longDesc = 
u"""


""",
)

entry(
    index = 8,
    label = "Ketene",
    group =
"""
1 * Cdd	0 	{2,D} {3,D}
2   Od  0 	{1,D}
3   C	X	{1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2110, 2130, 1),	#OdC stretch
            (495, 530, 1),		#OdCdC bend
            (650, 925, 1),		#OdCdC bend
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon with one carbon double bond and one oxygen double bond""",
    longDesc = 
u"""


""",
)

entry(
    index = 7,
    label = "Cumulene",
    group =
"""
1 * C 0       {2,D} {3,D}
2   C X {1,D}
3   C X {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (540, 610, 2),	#C-C-C scissor
            (1970, 2140, 1),#C-C-C asymmetric
        ],
        symmetry = 2,
    ),
    shortDesc = u"""Carbon with two double bonds to carbons""",
    longDesc = 
u"""


""",
)

entry(
    index = 5,
    label = "CdCHsR",
    group =
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   X {1,D}
3   R!H X {1,S}
4   H   0       {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2995, 3025, 1),	#C-H stretch
            (975, 1000, 1),		#R-C-H bend
            (1300, 1375, 1),	#R-C-H bend
            (400, 500, 1),		#CdC-R scissor
            (1630, 1680, 1),	#CdC stretch
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon with a double bond to carbon and a single bond to R""",
    longDesc = 
u"""


""",
)

entry(
    index = 9,
    label = "CtCsR",
    group =
"""
1 * C   0       {2,T} {3,S}
2   C   X       {1,T}
3   R!H X {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2100, 2250, 1),	#CtC stretch
            (500, 550, 1),		#CtC-C bend
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon with one triplet bond and one single bond""",
    longDesc = 
u"""


""",
)

entry(
    index = 10,
    label = "RsCHsR2",
    group =
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H X       {1,S}
3   R!H X       {1,S}
4   R!H X		{1,S}
5   H   0       {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1380, 1390, 2),	#R-C-H bend
            (370, 380, 2),		#C-C-C scissor
            (2800, 3000, 1),	#C-H stretch
            (430, 440, 1),		#Umbrella
        ],
        symmetry = 6,
    ),
    shortDesc = u"""carbon with three single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 11,
    label = "CdCsR2",
    group =
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C	X 		{1,D}
3   R!H X 		{1,S}
4   R!H X 		{1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (325, 375, 1),	#R-C-R scissor
            (415, 465, 1),	#CdC-R scissor
            (420, 450, 1),	#Umbrella
            (1700, 1750, 1),#CdC stretch
        ],
        symmetry = 2,
    ),
    shortDesc = u"""carbon with one carbon double bond and two single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 12,
    label = "Ketone",
    group =
"""
1 * C 0       {2,D} {3,S} {4,S}
2   O 0       {1,D}
3   C X 	{1,S}
4   C X 	{1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (365, 385, 1),	#R-C-R scissor
            (505, 600, 1),	#OdC-R scissor
            (445, 480, 1),	#Umbrella
            (1700, 1720, 1),#OdC stretch
        ],
        symmetry = 2,
    ),
    shortDesc = u"""carbon with one oxygen double bond and two single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 13,
    label = "CsCsC3",
    group =
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   C X       {1,S}
3   C X       {1,S}
4   C X {1,S}
5   C X {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 400, 2),	#C-C-C scissor
            (1190, 1240, 2),#C-C-C bend
            (400, 500, 1),	#Umbrella
        ],
        symmetry = 12,
    ),
    shortDesc = u"""carbon with four single bonds to carbon""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R1",
    group = 
"""
1 * C 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 14,
    label = "RsCH2r",
    group =
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H X {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3000, 3100, 2),	#C-H stretch
            (415, 465, 1),		#R-C-H swing
            (780, 850, 1),		#R-C-H rock
            (1435, 1475, 1),	#R-C-H scissor
            (900, 1100, 1),		
        ],
        symmetry = 2,
    ),
    shortDesc = u"""Carbon radical with one single bond""",
    longDesc = 
u"""


""",
)

entry(
    index = 15,
    label = "RdCHr",
    group =
"""
1 * C   1       {2,D} {3,S}
2   R!H X {1,D}
3   H   0       {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3115, 3125, 1),	#C-H stretch
            (620, 680, 1),		#CdC-H bend
            (785, 800, 1),		#CdC-H bend
            (1600, 1700, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon radical with one single bond""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCr",
    group =
"""
1 * C 1 {2,T}
2   C X {1,T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 16,
    label = "RsCHrsR",
    group =
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H X {1,S}
3   R!H X {1,S}
4   H   0       {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3000, 3050, 1),	#C-H stretch
            (390, 425, 1),		#R-C-H bend
            (1340, 1360, 1),	#R-C-H bend
            (335, 370, 1),		#R-C-R scissor
        ],
        symmetry = 2,
    ),
    shortDesc = u"""carbon radical with two single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 18,
    label = "OdCrsR",
    group =
"""
1 * C   1       {2,D} {3,S}
2   O   0       {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1850, 1860, 1),	#OdC stretch
            (440, 470, 1),		#OdC-R bend
            (900, 1000, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon radical with one oxygen double bond and one single bond""",
    longDesc = 
u"""


""",
)

entry(
    index = 17,
    label = "CdCrsR",
    group =
"""
1 * C   1 {2,D} {3,S}
2   C   X {1,D}
3   R!H X {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1670, 1700, 1),	#CdC stretch
            (300, 440, 1),		#CdC-R bend
        ],
        symmetry = 1,
    ),
    shortDesc = u"""carbon radical with one carbon double bond and one single bond""",
    longDesc = 
u"""


""",
)

entry(
    index = 19,
    label = "RsCrsR2",
    group =
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H X       {1,S}
3   R!H X       {1,S}
4   R!H X {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (360, 370, 2),	#C-C-C scissor
            (300, 400, 1),	#Umbrella
        ],
        symmetry = 6,
    ),
    shortDesc = u"""carbon radical with three single bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R2",
    group = 
"""
1 * C {2S,2T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrr",
    group =
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H X {1,S}
3   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCrr",
    group = 
"""
1 * C   {2S,2T} {2,D}
2   R!H {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsR",
    group =
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H X {1,S}
3   R!H X {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "O_R0",
    group = 
"""
1 * O 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 20,
    label = "Alcohol",
    group =
"""
1 * O 0 {2,S} {3,S}
2   C X {1,S}
3   H 0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3580, 3650, 1),	#O-H stretch
            (1210, 1345, 1),	#R-O-H bend
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""Oxygen with a single bond to hydrogen and another single bond to carbon""",
    longDesc = 
u"""


""",
)

entry(
    index = 21,
    label = "Ether",
    group =
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   C {2S,2T} {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),	#C-O-C scissor
        ],
        symmetry = 2,
    ),
    shortDesc = u"""oxygen with two single carbon bonds""",
    longDesc = 
u"""


""",
)

entry(
    index = 22,
    label = "COOH",
    group =
"""
1 * O 0       {2,S} {3,S}
2   C X {1,S}
3   O 0       {1,S} {4,S}
4   H 0       {3,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3580, 3650, 1),	#O-H stretch
            (1300, 1320, 1),	#O-O-H bend
            (350, 425, 1),		#C-O-O scissor
            (825, 875, 1),		#O-O stretch
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""Peroxide""",
    longDesc = 
u"""


""",
)

entry(
    index = 23,
    label = "COOC",
    group =
"""
1 * O 0       {2,S} {3,S}
2   C X {1,S}
3   O 0       {1,S} {4,S}
4   C X {3,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),	#C-O-O scissor
            (795, 815, 1),	#O-O stretch
        ],
        symmetry = 2,
    ),
    shortDesc = u"""peroxide""",
    longDesc = 
u"""


""",
)

entry(
    index = 24,
    label = "Peroxy",
    group =
"""
1 * O 0       {2,S} {3,S}
2   C X {1,S}
3   O 1       {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (470, 515, 1),	#C-O-O scissor
            (1100, 1170, 1),#O-O stretch
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""Oxygen single bonded to one carbon and one oxygen""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "O_R1",
    group = 
"""
1 * O 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Oxy",
    group =
"""
1 * O 1       {2,S}
2   C X {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "N_R0",
    group = 
"""
1 * N 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 25,
    label = "Amide_pri",
    group = "OR{Amide_prix0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3480, 3540, 1), # asymmetric N-H stretch, (free) primary amides
            (3380, 3420, 1), # symmetric N-H stretch, (free) primary amides
            (1670, 1690, 1), # C=O stretch, known as amide I band, primary amides (dilute solution)
            (1590, 1620, 1), # , primary amides (dilute solution)
            (1400, 1420, 1), # C-N stretch, known as amide III band, primary amides
            (1140, 1160, 1), # NH2 in-plane rocking vibration, primary amides
            (600, 750, 1),   # br. NH2 deformation vibration, primary amides
            (550, 600, 1),   # N-C=O deformation vibration, primary amides
            (450, 500, 1),   # C-C=O deformation vibration, primary amides
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3480, 3540, 1), # asymmetric N-H stretch, (free) primary amides
(3380, 3420, 1), # symmetric N-H stretch, (free) primary amides
(1670, 1690, 1), # C=O stretch, known as amide I band, primary amides (dilute solution)
(1590, 1620, 1), # , primary amides (dilute solution)
(1400, 1420, 1), # C-N stretch, known as amide III band, primary amides
(1140, 1160, 1), # NH2 in-plane rocking vibration, primary amides
(600, 750, 1),   # br. NH2 deformation vibration, primary amides
(550, 600, 1),   # N-C=O deformation vibration, primary amides
(450, 500, 1),   # C-C=O deformation vibration, primary amides
""",
)

entry(
    index = -1,
    label = "Amide_prix0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   H   0 {1,S}
6   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 26,
    label = "Amide_sec",
    group = "OR{Amide_secx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3420, 3460, 1), # N-H stretch, trans form (in dilute solution)
            (1510, 1550, 1), # amide II band, trans form (in dilute solution)
            (1665, 1700, 1), # C=O stretch, secondary amides (dilute solution)
            (1200, 1305, 1), # amide III band, secondary amides (trans form)
            (620, 770, 1),   # br. out-of-plane N-H, secondary amides (trans form)
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3420, 3460, 1), # N-H stretch, trans form (in dilute solution)
(1510, 1550, 1), # amide II band, trans form (in dilute solution)
(1665, 1700, 1), # C=O stretch, secondary amides (dilute solution)
(1200, 1305, 1), # amide III band, secondary amides (trans form)
(620, 770, 1),   # br. out-of-plane N-H, secondary amides (trans form)
""",
)

entry(
    index = -1,
    label = "Amide_secx0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   C   0 {1,S}
6   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 27,
    label = "Amide_ter",
    group = "OR{Amide_terx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1630, 1670, 1), # C=O stretch, tertiary amides (dilute solution or solid phase)
            (700, 870, 1), # asymmetric CNC stretch, tertiary amides
            (570, 620, 1), # , tertiary amides
            (440, 480, 1), # , tertiary amides
            (320, 390, 1), # , tertiary amides
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1630, 1670, 1), # C=O stretch, tertiary amides (dilute solution or solid phase)
(700, 870, 1), # asymmetric CNC stretch, tertiary amides
(570, 620, 1), # , tertiary amides
(440, 480, 1), # , tertiary amides
(320, 390, 1), # , tertiary amides
""",
)

entry(
    index = -1,
    label = "Amide_terx0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   C   0 {1,S}
6   C   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 28,
    label = "Imide",
    group = "OR{Imidex0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3200, 3280, 1), # N-H stretch, Imides (solid phase)
            (1670, 1740, 1), # C=O stretch, amide I band, Imides (solid phase)
            (1500, 1510, 1), # br., amide II band, Imides (solid phase)
            (1165, 1235, 1), # amide III band, Imides (solid phase)
            (730, 740, 1),   # br. N-H wagging, amide II band, Imides (solid phase)
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3200, 3280, 1), # N-H stretch, Imides (solid phase)
(1670, 1740, 1), # C=O stretch, amide I band, Imides (solid phase)
(1500, 1510, 1), # br., amide II band, Imides (solid phase)
(1165, 1235, 1), # amide III band, Imides (solid phase)
(730, 740, 1),   # br. N-H wagging, amide II band, Imides (solid phase)
""",
)

entry(
    index = -1,
    label = "Imidex0",
    group = 
"""
1 * N   0 {2,S} {3,S} {6,S}
2   H   0 {1,S}
3   C   0 {1,S} {4,D} {5,S}
4   O   0 {3,D}
5   R   0 {3,S}
6   C   0 {1,S} {7,D} {8,S}
7   O   0 {6,D}
8   R   0 {6,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 29,
    label = "Amine_pri",
    group = "OR{Amine_prix0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3330, 3550, 1), # asymmetric NH2 stretch, primary amines
            (3250, 3450, 1), # symmetric NH2 stretch, primary amines
            (1580, 1650, 1), # br. scissor vibration, saturated primary amines
            (1145, 1295, 1), # NH2 rocking/twisting vibration, saturated primary amines
            (650, 895, 1), # N-H bending out of plane, saturated primary amines
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3330, 3550, 1), # asymmetric NH2 stretch, primary amines
(3250, 3450, 1), # symmetric NH2 stretch, primary amines
(1580, 1650, 1), # br. scissor vibration, saturated primary amines
(1145, 1295, 1), # NH2 rocking/twisting vibration, saturated primary amines
(650, 895, 1), # N-H bending out of plane, saturated primary amines
""",
)

entry(
    index = -1,
    label = "Amine_prix0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 30,
    label = "Amine_sec",
    group = "OR{Amine_secx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3400, 3450, 1), # , secondary amines
            (1490, 1580, 1), # , secondary amines
            (700, 750, 1), # br. N-H wagging vibration, secondary amines
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3400, 3450, 1), # , secondary amines
(1490, 1580, 1), # , secondary amines
(700, 750, 1), # br. N-H wagging vibration, secondary amines
""",
)

entry(
    index = -1,
    label = "Amine_secx0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   C   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 31,
    label = "Amine_ter",
    group = "OR{Amine_terx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1020, 1250, 2),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Amine_terx0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   C   0 {1,S}
4   C   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 32,
    label = "Nitrile",
    group =
"""
1 * N   0       {2,T}
2   C   0       {1,T} {3,S}
3   C   X		 {2,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2230, 2260, 1), # C#N stretching, saturated aliphatic nitriles
            (340, 390, 1),   # C#N deformation, aliphatic nitriles
            (200, 160, 1),   # C#N deformation, aliphatic nitriles
        ],
        symmetry = 1,
    ),
    shortDesc = u"""N triple bonded to a carbon and single bonded to another carbon""",
    longDesc = 
u"""
(2230, 2260, 1), # C#N stretching, saturated aliphatic nitriles
(340, 390, 1),   # C#N deformation, aliphatic nitriles
(200, 160, 1),   # C#N deformation, aliphatic nitriles
""",
)


entry(
    index = 33,
    label = "Nitroso",
    group =
"""
1 * N   0       {2,D} {3,S}
2   O   0       {1,D}
3   R!H X		{1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1330, 1425, 1), # aliphatic compounds
            (1320, 1345, 1), # aliphatic compounds
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1330, 1425, 1), # aliphatic compounds
(1320, 1345, 1), # aliphatic compounds
""",
)

entry(
    index = 34,
    label = "Nitrites",
    group = "OR{Nitritesx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3220, 3360, 1), # Overtones of N=O stretch, nitrite compounds
            (1650, 1680, 1), # N=O stretch, nitrites, trans form
            (750, 815, 1),   # N-O stretch trans form, saturated primary and secondary aliphatic nitro compounds
            (565, 625, 1),   # O-N=O deformation vibration, saturated primary and secondary aliphatic nitro compounds
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3220, 3360, 1), # Overtones of N=O stretch, nitrite compounds
(1650, 1680, 1), # N=O stretch, nitrites, trans form
(750, 815, 1),   # N-O stretch trans form, saturated primary and secondary aliphatic nitro compounds
(565, 625, 1),   # O-N=O deformation vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = -1,
    label = "Nitritesx0",
    group = 
"""
1 * N 0 {2,D} {3,S}
2   O 0 {1,D}
3   O 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 35,
    label = "Nitro",
    group =
"""
1 * N   0 {2,D} {3,S} {4,S}
2   O   0 {1,D}
3   O   0 {1,S}
4   R!H 1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1545, 1555, 1), # asymmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
            (1360, 1385, 1), # symmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
            (915, 1000, 1),  # C-N stretch trans form, saturated primary and secondary aliphatic nitro compounds
            (850, 920, 1),  # br. C-N stretch gauche form, saturated primary and secondary aliphatic nitro compounds
            (605, 655, 1),  # NO2 deformation vibration, saturated primary and secondary aliphatic nitro compounds
            (470, 560, 1),  # NO2 rocking vibration, saturated primary and secondary aliphatic nitro compounds
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""  
(1545, 1555, 1), # asymmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(1360, 1385, 1), # symmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(915, 1000, 1),  # C-N stretch trans form, saturated primary and secondary aliphatic nitro compounds
(850, 920, 1),  # br. C-N stretch gauche form, saturated primary and secondary aliphatic nitro compounds
(605, 655, 1),  # NO2 deformation vibration, saturated primary and secondary aliphatic nitro compounds
(470, 560, 1),  # NO2 rocking vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = 36,
    label = "Nitrates",
    group = "OR{Nitratesx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1615, 1660, 1), # asymmetric NO2 stretch, Nitrates, -ONO2
            (1250, 1300, 1), # symmetric NO2 stretch, Nitrates, -ONO2
            (840, 870, 1),   # br.N-O stretch, Nitrates, -ONO2
            (745, 765, 1),   # NO2 out-of-plane deformation vibration, Nitrates, -ONO2
            (680, 720, 1),   # NO2 deformation vibration, Nitrates, -ONO2
            (560, 610, 1),   # NO2 in-plane deformation vibration, Nitrates, -ONO2
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1615, 1660, 1), # asymmetric NO2 stretch, Nitrates, -ONO2
(1250, 1300, 1), # symmetric NO2 stretch, Nitrates, -ONO2
(840, 870, 1),   # br.N-O stretch, Nitrates, -ONO2
(745, 765, 1),   # NO2 out-of-plane deformation vibration, Nitrates, -ONO2
(680, 720, 1),   # NO2 deformation vibration, Nitrates, -ONO2
(560, 610, 1),   # NO2 in-plane deformation vibration, Nitrates, -ONO2
""",
)

entry(
    index = -1,
    label = "Nitratesx0",
    group = 
"""
1 * N 0 {2,D} {3,S} {4,S}
2   O 0 {1,D}
3   O 0 {1,S}
4   O 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

tree(
"""
L1: R!H
	L2: R!Hx0
		L3: C_R0
			L4: RsCH3
			L4: RdCH2
			L4: CtCH
			L4: RsCH2sR
			L4: Aldehyde
			L4: Ketene
			L4: Cumulene
			L4: CdCHsR
			L4: CtCsR
			L4: RsCHsR2
			L4: CdCsR2
			L4: Ketone
			L4: CsCsC3
		L3: O_R0
			L4: Alcohol
			L4: Ether
			L4: COOH
			L4: COOC
			L4: Peroxy
		L3: N_R0
			L4: Amide_pri
				L5: Amide_prix0
			L4: Amide_sec
				L5: Amide_secx0
			L4: Amide_ter
				L5: Amide_terx0
			L4: Imide
				L5: Imidex0
			L4: Amine_pri
				L5: Amine_prix0
			L4: Amine_sec
				L5: Amine_secx0
			L4: Amine_ter
				L5: Amine_terx0
			L4: Nitrile
			L4: Nitroso
				L5: Nitrites
					L6: Nitritesx0
				L5: Nitro
					L6: Nitrates
						L7: Nitratesx0
	L2: R!Hx1
		L3: C_R1
			L4: RsCH2r
			L4: RdCHr
			L4: CtCr
			L4: RsCHrsR
			L4: OdCrsR
			L4: CdCrsR
			L4: RsCrsR2
		L3: O_R1
			L4: Oxy
	L2: R!Hx2
		L3: C_R2
			L4: RsCHrr
			L4: RdCrr
			L4: RsCrrsR
	L2: R!Hx3

"""
)

