#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C5H11O2 <=> C5H10O + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.29e+09,'s^-1'), n=0.67, Ea=(18.154,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC([CH2])COO <=> OH + C1OCC1CC
""",
)

entry(
    index = 2,
    label = "C5H11O2-2 <=> C5H10O-2 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.4e+10,'s^-1'), n=0.73, Ea=(12.459,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC[C](C)COO <=> OH + C1OC1(C)CC
""",
)

entry(
    index = 3,
    label = "C5H11O2-3 <=> C5H10O-3 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+09,'s^-1'), n=0.84, Ea=(17.137,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: C[CH]C(C)COO <=> OH + CC1OCC1C
""",
)

entry(
    index = 4,
    label = "C5H11O2-4 <=> C5H10O-4 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.41e+08,'s^-1'), n=0.84, Ea=(11.715,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: [CH2]CC(C)COO <=> OH + CC1CCOC1
""",
)

entry(
    index = 5,
    label = "C5H11O2-5 <=> C5H10O-5 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.56e+11,'s^-1'), n=0.59, Ea=(13.83,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC(C)[CH]COO <=> OH + C1OC1C(C)C
""",
)

entry(
    index = 6,
    label = "C5H11O2-6 <=> C5H10O-6 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.33e+07,'s^-1'), n=1.16, Ea=(15.287,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: C[C](C)CCOO <=> OH + O1CCC1(C)C
""",
)

entry(
    index = 7,
    label = "C5H11O2-7 <=> C5H10O-7 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.63e+08,'s^-1'), n=0.89, Ea=(11.911,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: [CH2]C(C)CCOO <=> OH + CC1CCOC1
""",
)

entry(
    index = 8,
    label = "C5H11O2-8 <=> C5H10O-8 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.98e+09,'s^-1'), n=1.03, Ea=(13.191,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CC(C)C([CH2])OO <=> OH + C1OC1C(C)C
""",
)

entry(
    index = 9,
    label = "C5H11O2-9 <=> C5H10O-9 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+12,'s^-1'), n=0.42, Ea=(10.506,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: C[C](C)C(C)OO <=> OH + CC1OC1(C)C
""",
)

entry(
    index = 10,
    label = "C5H11O2-10 <=> C5H10O-10 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.79e+09,'s^-1'), n=0.85, Ea=(16.351,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: [CH2]C(C)C(C)OO <=> OH + CC1OCC1C
""",
)

entry(
    index = 11,
    label = "C5H11O2-11 <=> C5H10O-11 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.43e+10,'s^-1'), n=0.75, Ea=(12.588,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: CCC(C)([CH2])OO <=> OH + C1OC1(C)CC
""",
)

entry(
    index = 12,
    label = "C5H11O2-12 <=> C5H10O-12 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.36e+08,'s^-1'), n=1.01, Ea=(17.108,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: [CH2]CC(C)(C)OO <=> OH + O1CCC1(C)C
""",
)

entry(
    index = 13,
    label = "C5H11O2-13 <=> C5H10O-13 + HO",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.21e+10,'s^-1'), n=0.69, Ea=(11.244,'kcal/mol'), T0=(1,'K'), Tmin=(400,'K'), Tmax=(1500,'K')),
    rank = 3,
    shortDesc = """calculated at QCISD(T)/CBS//B3LYP/6-311++G(d,p) 1DHR from [4] by Ye et al.""",
    longDesc = 
"""
Training reaction from kinetics library: alkene_chemistry
Original entry: C[CH]C(C)(C)OO <=> OH + CC1OC1(C)C
""",
)

