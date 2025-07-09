#!/usr/bin/env python
# encoding: utf-8

name = "Cation_R_Recombination/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[33460.9,-0.743262,-0.00216677,8.22742e-07], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 5 training reactions at node Root"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 5 training reactions at node Root""",
    longDesc = 
"""
Marcus rule fitted to 5 training reactions at node Root
""",
)

entry(
    index = 2,
    label = "Root_2R->C",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[51487.7,-0.166019,-0.00176034,4.42738e-07], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 2 training reactions at node Root_2R->C"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 2 training reactions at node Root_2R->C""",
    longDesc = 
"""
Marcus rule fitted to 2 training reactions at node Root_2R->C
""",
)

entry(
    index = 3,
    label = "Root_N-2R->C",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[21443.1,-1.12809,-0.00243772,1.07608e-06], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 3 training reactions at node Root_N-2R->C"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 3 training reactions at node Root_N-2R->C""",
    longDesc = 
"""
Marcus rule fitted to 3 training reactions at node Root_N-2R->C
""",
)

entry(
    index = 4,
    label = "Root_2R->C_Ext-2C-R",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[51072.9,0.770449,0.00461441,-2.38037e-06], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R""",
    longDesc = 
"""
Marcus rule fitted to 1 training reactions at node Root_2R->C_Ext-2C-R
""",
)

entry(
    index = 5,
    label = "Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[22140,-3.52755,-0.00528491,2.76922e-06], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 1 training reactions at node Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 1 training reactions at node Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R""",
    longDesc = 
"""
Marcus rule fitted to 1 training reactions at node Root_N-2R->C_Ext-2BrClFHILiNOPSSi-R
""",
)

entry(
    index = 6,
    label = "Root_N-2R->C_2BrClFHILiNOPSSi->S",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[20364.7,0.177444,-0.000702861,-3.39533e-08], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 1 training reactions at node Root_N-2R->C_2BrClFHILiNOPSSi->S"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 1 training reactions at node Root_N-2R->C_2BrClFHILiNOPSSi->S""",
    longDesc = 
"""
Marcus rule fitted to 1 training reactions at node Root_N-2R->C_2BrClFHILiNOPSSi->S
""",
)

entry(
    index = 7,
    label = "Root_N-2R->C_N-2BrClFHILiNOPSSi->S",
    kinetics = Marcus(A=(1.73e+06,'m^3/(mol*s)'), n=2, lmbd_i_coefs=[21824.5,-0.0341626,-0.0013254,4.92966e-07], beta=(1.2e+10,'1/m'), wr=(0,'kJ/mol'), wp=(0,'kJ/mol'), lmbd_o=(0,'J/mol'), comment="""Marcus rule fitted to 1 training reactions at node Root_N-2R->C_N-2BrClFHILiNOPSSi->S"""),
    rank = 11,
    shortDesc = """Marcus rule fitted to 1 training reactions at node Root_N-2R->C_N-2BrClFHILiNOPSSi->S""",
    longDesc = 
"""
Marcus rule fitted to 1 training reactions at node Root_N-2R->C_N-2BrClFHILiNOPSSi->S
""",
)

