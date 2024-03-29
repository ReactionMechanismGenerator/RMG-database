#!/usr/bin/env python
# encoding: utf-8

name = "Cation_Li_Abstraction/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusChargeTransfer(A=(62.0316,'m^3/(mol*s)'), n=2.36922, Ea=(79.4161,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=5.998356318514794e-16, var=505.91409392421104, Tref=1000.0, N=3, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 3 training reactions at node Root
    Total Standard Deviation in ln(k): 45.09157225395358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 45.09157225395358""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root
Total Standard Deviation in ln(k): 45.09157225395358
""",
)

entry(
    index = 2,
    label = "Root_2ClFH->H",
    kinetics = ArrheniusChargeTransferBM(A=(0.16967,'m^3/(mol*s)'), n=3.09275, w0=(329000,'J/mol'), E0=(32900,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2ClFH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2ClFH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2ClFH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_2ClFH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-2ClFH->H",
    kinetics = ArrheniusChargeTransferBM(A=(0.00259259,'m^3/(mol*s)'), n=3.67979, w0=(464500,'J/mol'), E0=(46450,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3891038420719923, var=3.145896398464165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2ClFH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2ClFH->H
    Total Standard Deviation in ln(k): 7.045944110173986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2ClFH->H
Total Standard Deviation in ln(k): 7.045944110173986""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_N-2ClFH->H
Total Standard Deviation in ln(k): 7.045944110173986
""",
)

entry(
    index = 4,
    label = "Root_N-2ClFH->H_2ClF->Cl",
    kinetics = ArrheniusChargeTransferBM(A=(4264.72,'m^3/(mol*s)'), n=1.78731, w0=(398000,'J/mol'), E0=(39800,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2ClFH->H_2ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_2ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_2ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_2ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-2ClFH->H_N-2ClF->Cl",
    kinetics = ArrheniusChargeTransferBM(A=(329.871,'m^3/(mol*s)'), n=2.2276, w0=(531000,'J/mol'), E0=(53100,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2ClFH->H_N-2ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_N-2ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_N-2ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-2ClFH->H_N-2ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)
