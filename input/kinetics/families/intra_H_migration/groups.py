#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["RnH"], products=["RnH"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

entry(
    index = 1,
    label = "RnH",
    group = "OR{R2H, R3H, R4H, R5H, R6H, R7H}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.50795e-16,3.28444e-09,4.50549e-05,0.0266116,81.7796,10592,7.65066e+06,2.21987e+08],"s^-1","*|/",[1.74371e+06,45797.1,5278.37,1275.68,226.829,84.8951,26.7225,17.338])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [262, 262, 262, 262, 262, 262, 262, 262] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=1 label="RnH">, <Entry index=2 label="Y_rad_out">, <Entry index=3 label="XH_out">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1  *1 R!H 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "XH_out",
    group = 
"""
1  *2 R!H 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "R2H",
    group = 
"""
1  *1 R!H 1 {2,{S,D,B}}
2  *2 R!H 0 {1,{S,D,B}} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0363224,0.117974,0.238977,0.382359,0.687297,0.976226,1.55563,1.96072],"s^-1","*|/",[534451,19045.1,2637.66,719.955,148.351,60.1852,20.4588,13.3398])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [70, 70, 70, 70, 70, 70, 70, 70] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "R2H_S",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *2 R!H 0 {1,S} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0309418,0.104162,0.215619,0.350046,0.640903,0.920601,1.48967,1.8926],"s^-1","*|/",[518756,19088.2,2694.91,745.008,155.919,63.8065,21.8774,14.2764])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [66, 66, 66, 66, 66, 66, 66, 66] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "R2H_S_cy3",
    group = 
"""
1  *1 R!H 1 {2,S} {4,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000728418,0.00844974,0.0361362,0.0941117,0.305004,0.606911,1.4634,2.20671],"s^-1","*|/",[112617,5033.71,815.425,250.124,60.7193,27.4841,10.9089,7.64282])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "R2H_S_cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {1,{S,D,B}} {4,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00998073,0.0454988,0.111,0.198718,0.402662,0.603924,0.996917,1.24189],"s^-1","*|/",[3.90978e+29,6.84412e+21,1.63876e+17,1.4325e+14,2.35758e+10,1.36647e+08,167598,6677.51])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "R2H_S_cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0484948,0.20463,0.474975,0.8207,1.58446,2.30055,3.61035,4.36011],"s^-1","*|/",[92420.7,3430.06,498.703,142.264,31.297,13.1725,4.51475,2.80364])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Others-R2H_S",
    group = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0401239,0.120949,0.234979,0.366365,0.63987,0.89599,1.40989,1.7748],"s^-1","*|/",[1.36434e+06,39017.4,4729.51,1179.93,216.767,81.8853,25.1604,15.5423])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [56, 56, 56, 56, 56, 56, 56, 56] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "R2H_D",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11.8723,10.582,9.80425,9.27272,8.57427,8.12119,7.43722,7.03032],"s^-1","*|/",[1.28983e+11,9.86196e+07,1.3589e+06,79379.7,2361.99,298.286,21.8164,7.37132])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "R2H_B",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *2 Cb 0 {1,B} {3,S}
3  *3 H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "R3H",
    group = "OR{R3H_SR, R3H_MS, R3H_BB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0479365,0.103609,0.164574,0.224092,0.329731,0.415843,0.566976,0.66237],"s^-1","*|/",[7.43485e+06,138582,12782.8,2623.29,366.791,114.191,25.1128,12.3242])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [128, 128, 128, 128, 128, 128, 128, 128] rates.
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "R3H_SR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{S,D,T,B}}
3  *2 R!H 0 {2,{S,D,T,B}} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0452537,0.0990406,0.158515,0.216946,0.321287,0.406799,0.55767,0.653354],"s^-1","*|/",[1.12168e+07,188634,16356.8,3221.14,427.748,129.116,27.2573,13.1127])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [121, 121, 121, 121, 121, 121, 121, 121] rates.
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "R3H_SS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0865619,0.15979,0.230934,0.29529,0.401737,0.483462,0.619478,0.70178],"s^-1","*|/",[2.09568e+06,54090.5,6080.67,1426.42,236.597,81.8912,20.9105,11.1244])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [114, 114, 114, 114, 114, 114, 114, 114] rates.
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "R3H_SS_12cy3",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.14891e+06,48721.4,7099.74,1927.52,364.663,130.344,31.0256,14.3975],"s^-1","*|/",[1.58235e+21,7.74608e+15,5.18752e+12,4.06215e+10,9.95753e+07,2.85376e+06,29284.6,3483.24])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "R3H_SS_23cy3",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.61675e-05,0.000234441,0.00117585,0.00346372,0.0134944,0.0307614,0.0938824,0.166238],"s^-1","*|/",[2.21874e+07,367620,30841,5838.78,713.249,198.241,34.5298,13.9688])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 17,
    label = "R3H_SS_12cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.152589,0.245056,0.319559,0.376694,0.452517,0.49575,0.537863,0.542825],"s^-1","*|/",[698.316,125.133,44.3159,22.1188,9.26841,5.52422,2.87773,2.22562])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "R3H_SS_23cy4",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0176927,0.0489706,0.0917466,0.141011,0.246209,0.349868,0.579581,0.767555],"s^-1","*|/",[224.132,57.7344,25.6119,14.8997,7.5636,5.02731,2.90149,2.19949])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "R3H_SS_13cy4",
    group = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.5053e-12,6.43745e-09,3.12518e-07,4.08152e-06,9.79988e-05,0.000641464,0.00739369,0.0239359],"s^-1","*|/",[10385.1,875.306,201.789,76.8576,23.6402,11.9861,5.23522,3.72178])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "R3H_SS_12cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.154085,0.277325,0.388397,0.481118,0.617119,0.705326,0.814932,0.853048],"s^-1","*|/",[627.069,127.786,49.459,26.4049,12.2119,7.8084,4.50659,3.58608])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "R3H_SS_23cy5",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.817903,0.735947,0.704053,0.692263,0.693249,0.707183,0.756352,0.807655],"s^-1","*|/",[22534.3,1954.25,445.419,164.896,46.946,21.8259,7.66149,4.4541])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 22,
    label = "R3H_SS_13cy5",
    group = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.48126e-06,0.000105037,0.000797944,0.00305015,0.0159888,0.042499,0.151086,0.27711],"s^-1","*|/",[14116.9,1117.74,246.308,90.4251,26.1411,12.5426,4.82383,3.05356])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 23,
    label = "R3H_SS_2Cd",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.06016e-08,3.77147e-06,6.82515e-05,0.000472716,0.00535708,0.0231562,0.165589,0.448224],"s^-1","*|/",[16457,1286.5,279.547,101.289,28.6546,13.5423,5.15012,3.33444])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [9, 9, 9, 9, 9, 9, 9, 9] rates.
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 24,
    label = "R3H_SS_OC",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0121551,0.0482077,0.111444,0.196314,0.403783,0.629491,1.16582,1.61707],"s^-1","*|/",[3005.25,545.107,201.783,106.523,50.2471,33.39,21.155,17.9314])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "Others-R3H_SS",
    group = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([8.44009,4.17782,2.75623,2.09711,1.50084,1.23529,0.965104,0.861699],"s^-1","*|/",[2.04848e+07,294611,23377.9,4354.66,542.839,158.605,32.4118,15.4522])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [51, 51, 51, 51, 51, 51, 51, 51] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "R3H_SD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.26376e-09,4.08675e-07,9.21262e-06,7.3413e-05,0.00098043,0.00463318,0.0365753,0.102397],"s^-1","*|/",[1.74288e+19,2.36241e+14,2.79565e+11,3.09934e+09,1.0976e+07,366849,3856.31,389.563])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "R3H_ST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Ct 0 {1,S} {3,T}
3  *2 Ct 0 {2,T} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "R3H_SB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *2 Cb 0 {2,B} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "R3H_MS",
    group = 
"""
1  *1 R!H 1 {2,{D,T,B}}
2  *4 R!H 0 {1,{D,T,B}} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.225935,0.34877,0.451769,0.536207,0.662915,0.751583,0.885225,0.957901],"s^-1","*|/",[1399.45,216.484,71.9852,35.0412,14.6629,8.93663,4.93715,3.87544])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "R3H_DS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.225935,0.34877,0.451769,0.536207,0.662915,0.751583,0.885225,0.957901],"s^-1","*|/",[1399.45,216.484,71.9852,35.0412,14.6629,8.93663,4.93715,3.87544])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "R3H_TS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "R3H_BS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "R3H_BB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3  *2 Cb 0 {2,B} {4,S}
4  *3 H 0 {3,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "R4H",
    group = "OR{R4H_RSR, R4H_SMS, R4H_SBB, R4H_BBS, R4H_BBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.97615e+07,452297,20325.7,2570.93,194.165,41.2537,5.24167,1.87163],"s^-1","*|/",[733305,18783.5,2152.27,521.832,94.8055,36.7728,13.2044,9.9661])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [27, 27, 27, 27, 27, 27, 27, 27] rates.
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "R4H_RSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 R!H 0 {2,S} {4,{S,D,T,B}}
4  *2 R!H 0 {3,{S,D,T,B}} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1","*|/",[928332,21174.6,2270.08,527.87,91.6208,34.8731,12.5871,9.79081])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 36,
    label = "R4H_RSS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1","*|/",[928332,21174.6,2270.08,527.87,91.6208,34.8731,12.5871,9.79081])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 37,
    label = "R4H_SSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.14217e+08,937067,35947.5,4084.77,269.012,52.5148,5.92794,1.98664],"s^-1","*|/",[928332,21174.6,2270.08,527.87,91.6208,34.8731,12.5871,9.79081])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [24, 24, 24, 24, 24, 24, 24, 24] rates.
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "R4H_SSS_OOCsCs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([54765,2908.72,496.024,151.763,34.2234,13.8963,4.11069,2.20722],"s^-1","*|/",[6477.61,675.492,178.192,74.724,26.3347,14.754,7.74779,6.29939])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "R4H_SSS_OO(Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([74648.8,3793.08,628.866,188.626,41.415,16.5225,4.75764,2.51362],"s^-1","*|/",[11732,948.023,211.813,78.8761,23.684,11.9907,5.59236,4.45707])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([36785.1,2190.83,398.894,127.221,30.1032,12.541,3.81261,2.06417],"s^-1","*|/",[7.64594e+08,2.18684e+06,62955.5,5807.12,290.257,48.7971,6.19392,5.12907])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 41,
    label = "R4H_DSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "R4H_TSS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "R4H_BSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "R4H_RSD",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "R4H_SSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "R4H_DSD",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "R4H_TSD",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "R4H_BSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Cd 0 {2,S} {4,D}
4  *2 Cd 0 {3,D} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "R4H_RST",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    label = "R4H_SST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    label = "R4H_DST",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "R4H_TST",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    label = "R4H_BST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Ct 0 {2,S} {4,T}
4  *2 Ct 0 {3,T} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "R4H_RSB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "R4H_SSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "R4H_DSB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "R4H_TSB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "R4H_BSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3  *5 Cb 0 {2,S} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "R4H_SMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 {Cd,Ct,Cb} 0 {1,S} {3,{D,T,B}}
3  *5 {Cd,Ct,Cb} 0 {2,{D,T,B}} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2238.79,199.249,47.9842,18.9198,6.10902,3.18769,1.42103,0.994171],"s^-1","*|/",[5.03103e+13,2.88815e+10,3.22123e+08,1.59813e+07,376009,40536,2340.88,660.398])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 60,
    label = "R4H_SDS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *5 Cd 0 {2,D} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2238.79,199.249,47.9842,18.9198,6.10902,3.18769,1.42103,0.994171],"s^-1","*|/",[5.03103e+13,2.88815e+10,3.22123e+08,1.59813e+07,376009,40536,2340.88,660.398])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 61,
    label = "R4H_STS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Ct 0 {1,S} {3,T}
3  *5 Ct 0 {2,T} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "R4H_SBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *5 Cb 0 {2,B} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    label = "R4H_SBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3  *5 Cbf 0 {2,B} {4,B}
4  *2 Cb 0 {3,B} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    label = "R4H_BBS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3  *5 Cb 0 {2,B} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    label = "R4H_BBB",
    group = 
"""
1  *1 Cb 1 {2,B} {15,B}
2  *4 Cbf 0 {1,B} {3,B} {12,B}
3  *5 Cbf 0 {2,B} {4,B} {9,B}
4  *2 Cb 0 {3,B} {5,S} {6,B}
5  *3 H 0 {4,S}
6     {Cb,Cbf} 0 {4,B} {7,B}
7     {Cb,Cbf} 0 {6,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     Cbf 0 {3,B} {8,B} {10,B}
10    {Cb,Cbf} 0 {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    Cbf 0 {2,B} {11,B} {13,B}
13    {Cb,Cbf} 0 {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {1,B} {14,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    label = "R5H",
    group = "OR{R5H_RSSR, R5H_RSMS, R5H_SMSR, R5H_BBSR, R5H_RSBB, R5H_SBBS, R5H_SBBB, R5H_BBBS, R5H_BBBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.12553e+11,2.30581e+08,2.57914e+06,129044,3055.68,323.573,16.2299,3.6383],"s^-1","*|/",[72746.3,4566.34,975.917,389.347,157.921,115.301,116.8,152.296])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [20, 20, 20, 20, 20, 20, 20, 20] rates.
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 67,
    label = "R5H_RSSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.56623e+11,2.95247e+08,3.1808e+06,154583,3504.09,359.253,17.0342,3.6746],"s^-1","*|/",[111252,6336.96,1290.78,503.236,201.946,148.595,155.394,208.239])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "R5H_SSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.56623e+11,2.95247e+08,3.1808e+06,154583,3504.09,359.253,17.0342,3.6746],"s^-1","*|/",[111252,6336.96,1290.78,503.236,201.946,148.595,155.394,208.239])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [18, 18, 18, 18, 18, 18, 18, 18] rates.
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 69,
    label = "R5H_SSSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.39879e+11,2.91669e+08,3.17162e+06,154920,3526.91,361.912,17.118,3.67753],"s^-1","*|/",[127471,7094.55,1435.97,560.973,228.237,170.607,183.769,250.924])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [17, 17, 17, 17, 17, 17, 17, 17] rates.
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 70,
    label = "R5H_SSSS_OOCCC",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.861e+11,4.97113e+08,6.04903e+06,322297,8355.35,943.699,52.7122,12.684],"s^-1","*|/",[2911.68,703.695,302.659,173.258,86.8635,57.6799,33.7268,26.0002])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 71,
    label = "R5H_SSSS_OO(Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.73929e+12,1.06568e+09,1.24918e+07,641298,15528.8,1652.83,82.0067,18.031],"s^-1","*|/",[3715.39,742.441,295.458,164.183,82.0411,55.6608,34.7642,28.3337])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 72,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S} {8,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
8     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.95621e+09,4.70179e+06,127131,11513.9,577.505,96.6575,9.06938,2.81579],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 73,
    label = "R5H_SSSS_OOCs(Cs/Cs)",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.29993e+09,1.60418e+07,414281,36578.7,1793.85,298.541,28.2702,8.93431],"s^-1","*|/",[462.743,1354.74,3645.22,8034.11,25315.2,56138.1,197834,429580])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 74,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs)",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S} {8,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
8     Cs 0 {4,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.41985e+10,3.15851e+07,819823,72520.5,3555.17,590.194,55.4327,17.3805],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 75,
    label = "R5H_SSSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.04638e+12,3.79864e+08,3.37667e+06,147784,3064.14,308.472,15.3924,3.61439],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 76,
    label = "R5H_SSST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "R5H_SSSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "R5H_DSSR",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "R5H_DSSS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "R5H_DSSD",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "R5H_DSST",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "R5H_DSSB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "R5H_TSSR",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "R5H_TSSS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "R5H_TSSD",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    label = "R5H_TSST",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    label = "R5H_TSSB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "R5H_BSSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "R5H_BSSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    label = "R5H_BSSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "R5H_BSST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "R5H_BSSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    label = "R5H_RSMS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.86828e+17,6.66514e+12,9.70148e+09,1.28717e+08,614157,26104.6,429.898,59.8986],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "R5H_SSMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    label = "R5H_DSMS",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.86828e+17,6.66514e+12,9.70148e+09,1.28717e+08,614157,26104.6,429.898,59.8986],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "R5H_TSMS",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    label = "R5H_BSMS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "R5H_SMSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5814.19,224.42,33.1728,9.52944,2.10355,0.885239,0.304678,0.191476],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 99,
    label = "R5H_SMSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    label = "R5H_SMSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5814.19,224.42,33.1728,9.52944,2.10355,0.885239,0.304678,0.191476],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 101,
    label = "R5H_SMST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "R5H_SMSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "R5H_BBSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 R!H 0 {3,S} {5,{S,D,T,B}}
5  *2 R!H 0 {4,{S,D,T,B}} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "R5H_BBSS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "R5H_BBSD",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "R5H_BBST",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Ct 0 {3,S} {5,T}
5  *2 Ct 0 {4,T} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    label = "R5H_BBSB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4  *5 Cb 0 {3,S} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    label = "R5H_RSBB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    label = "R5H_SSBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    label = "R5H_DSBB",
    group = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    label = "R5H_TSBB",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    label = "R5H_BSBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cb 0 {1,B} {3,S}
3     Cb 0 {2,S} {4,B}
4  *5 Cbf 0 {3,B} {5,B}
5  *2 Cb 0 {4,B} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    label = "R5H_SBBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4  *5 Cb 0 {3,B} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    label = "R5H_SBBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B} {16,B}
3     Cbf 0 {2,B} {4,B} {13,B}
4  *5 Cbf 0 {3,B} {5,B} {10,B}
5  *2 Cb 0 {4,B} {6,S} {7,B}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {2,B} {15,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    label = "R5H_BBBS",
    group = 
"""
1  *1 Cb 1 {2,B} {16,B}
2  *4 Cbf 0 {1,B} {3,B} {13,B}
3     Cbf 0 {2,B} {4,B} {10,B}
4  *5 Cb 0 {3,B} {5,S} {7,B}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {4,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {3,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {2,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    {Cb,Cbf} 0 {1,B} {15,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    label = "R5H_BBBB",
    group = 
"""
1  *1 Cb 1 {2,B} {19,B}
2  *4 Cbf 0 {1,B} {3,B} {16,B}
3     Cbf 0 {2,B} {4,B} {13,B}
4  *5 Cbf 0 {3,B} {5,B} {10,B}
5  *2 Cb 0 {4,B} {6,S} {7,B}
6  *3 H 0 {5,S}
7     {Cb,Cbf} 0 {5,B} {8,B}
8     {Cb,Cbf} 0 {7,B} {9,B}
9     {Cb,Cbf} 0 {8,B} {10,B}
10    Cbf 0 {4,B} {9,B} {11,B}
11    {Cb,Cbf} 0 {10,B} {12,B}
12    {Cb,Cbf} 0 {11,B} {13,B}
13    Cbf 0 {3,B} {12,B} {14,B}
14    {Cb,Cbf} 0 {13,B} {15,B}
15    {Cb,Cbf} 0 {14,B} {16,B}
16    Cbf 0 {2,B} {15,B} {17,B}
17    {Cb,Cbf} 0 {16,B} {18,B}
18    {Cb,Cbf} 0 {17,B} {19,B}
19    {Cb,Cbf} 0 {1,B} {18,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    label = "R6H",
    group = "OR{R6H_RSSSR, R6H_RSSMS, R6H_RSMSR, R6H_SMSSR, R6H_SMSMS, R6H_BBSRS, R6H_BBSSM, R6H_BBSBB, R6H_SBBSR, R6H_RSBBS, R6H_BBBSR, R6H_SBBBS, R6H_RSBBB, R6H_SBBBB, R6H_BBBBS, R6H_BBBBB}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1","*|/",[289307,16699.2,3265.82,1163.78,356.602,193.107,105.894,93.196])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 118,
    label = "R6H_RSSSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1","*|/",[289307,16699.2,3265.82,1163.78,356.602,193.107,105.894,93.196])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "R6H_SSSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1","*|/",[289307,16699.2,3265.82,1163.78,356.602,193.107,105.894,93.196])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "R6H_SSSSS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.4896e+11,8.15162e+07,667800,27318.7,508.575,47.0572,2.01177,0.423001],"s^-1","*|/",[289307,16699.2,3265.82,1163.78,356.602,193.107,105.894,93.196])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "R6H_SSSSS_OO",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.53812e+12,3.49201e+08,2.34953e+06,85582,1415.78,124.859,5.25731,1.13998],"s^-1","*|/",[424431,17237,2558.47,724.272,152.195,60.5836,18.3246,10.3531])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 122,
    label = "R6H_SSSSD",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "R6H_SSSST",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "R6H_SSSSB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    label = "R6H_DSSSR",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    label = "R6H_DSSSS",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    label = "R6H_DSSSD",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    label = "R6H_DSSST",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    label = "R6H_DSSSB",
    group = 
"""
1  *1 R!H 1 {2,D}
2  *4 R!H 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    label = "R6H_TSSSR",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    label = "R6H_TSSSS",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "R6H_TSSSD",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    label = "R6H_TSSST",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    label = "R6H_TSSSB",
    group = 
"""
1  *1 R!H 1 {2,T}
2  *4 R!H 0 {1,T} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    label = "R6H_BSSSR",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "R6H_BSSSS",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "R6H_BSSSD",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,D}
6  *2 R!H 0 {5,D} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "R6H_BSSST",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,T}
6  *2 R!H 0 {5,T} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    label = "R6H_BSSSB",
    group = 
"""
1  *1 R!H 1 {2,B}
2  *4 R!H 0 {1,B} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,B}
6  *2 R!H 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    label = "R6H_RSSMS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,{D,T,B}}
5  *5 R!H 0 {4,{D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "R6H_RSMSR",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4     R!H 0 {3,{D,T,B}} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    label = "R6H_SMSSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    label = "R6H_SMSMS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4     R!H 0 {3,S} {5,{D,T,B}}
5  *5 R!H 0 {4,{D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    label = "R6H_BBSRS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     R!H 0 {3,S} {5,{S,D,T,B}}
5  *5 R!H 0 {4,{S,D,T,B}} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    label = "R6H_BBSSM",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,{D,T,B}}
6  *2 R!H 0 {5,{D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "R6H_BBSBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cb 0 {2,B} {4,S}
4     Cb 0 {3,S} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    label = "R6H_SBBSR",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cb 0 {3,B} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    label = "R6H_RSBBS",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "R6H_BBBSR",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cb 0 {3,B} {5,S}
5  *5 R!H 0 {4,S} {6,{S,D,T,B}}
6  *2 R!H 0 {5,{S,D,T,B}} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    label = "R6H_SBBBS",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    label = "R6H_RSBBB",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,S}
3     Cb 0 {2,S} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "R6H_SBBBB",
    group = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cb 0 {1,S} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "R6H_BBBBS",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cb 0 {4,B} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    label = "R6H_BBBBB",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 Cbf 0 {1,B} {3,B}
3     Cbf 0 {2,B} {4,B}
4     Cbf 0 {3,B} {5,B}
5  *5 Cbf 0 {4,B} {6,B}
6  *2 Cb 0 {5,B} {7,S}
7  *3 H 0 {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    label = "R7H",
    group = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.79802e+09,1.85789e+06,22872.6,1213.9,30.6695,3.35131,0.172505,0.0386849],"s^-1","*|/",[6.00514e+09,3.4827e+07,1.70401e+06,239915,22796.5,6055.28,1255.11,666.589])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [8, 8, 8, 8, 8, 8, 8, 8] rates.
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 156,
    label = "R7H_OOCs4",
    group = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.14659e+11,9.00437e+07,575997,19967.7,301.881,24.6292,0.888419,0.171306],"s^-1","*|/",[96567.8,5112.29,934.806,319.01,95.2637,53.0774,33.7962,33.965])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 157,
    label = "O_rad_out",
    group = 
"""
1  *1 O 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.73852,5.58191,3.99931,3.20335,2.42883,2.05826,1.65243,1.48189],"s^-1","*|/",[51613.6,4514.58,1096.56,441.07,150.196,83.0331,42.3579,33.145])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [56, 56, 56, 56, 56, 56, 56, 56] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 158,
    label = "Cd_rad_out_double",
    group = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([70.538,27.1027,15.2911,10.4513,6.50698,4.90431,3.37504,2.80712],"s^-1","*|/",[1.70464e+09,7.28471e+06,276742,31371,2082,413.809,50.2043,18.5721])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 159,
    label = "Cd_rad_out_single",
    group = 
"""
1  *1 Cd 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([124.506,43.5597,23.2041,15.2516,9.02962,6.59518,4.34119,3.52404],"s^-1","*|/",[37587.3,2096.49,376.765,121.476,30.3458,13.6165,5.16199,3.55101])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [12, 12, 12, 12, 12, 12, 12, 12] rates.
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 160,
    label = "Cd_rad_out_singleH",
    group = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3078.61,473.668,153.919,72.7003,28.4318,16.1701,7.60241,5.20366],"s^-1","*|/",[640849,18462,2246.21,560.892,102.629,38.4396,11.5072,6.9611])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 161,
    label = "Cd_rad_out_singleNd",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([69.088,29.3126,17.5422,12.4661,8.14346,6.31388,4.50698,3.81435],"s^-1","*|/",[2.88581e+06,42400.9,3424.88,648.143,83.2558,25.1249,5.77141,3.35568])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 162,
    label = "Cd_rad_out_singleDe",
    group = 
"""
1  *1 Cd 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.16771e-06,3.63589e-05,0.000287786,0.00114736,0.00650781,0.0185426,0.0758252,0.15482],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 163,
    label = "Ct_rad_out",
    group = 
"""
1  *1 Ct 1 {2,T}
2  *4 Ct 0 {1,T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    label = "Cb_rad_out",
    group = 
"""
1  *1 Cb 1 {2,B}
2  *4 {Cb,Cbf} 0 {1,B}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    label = "CO_rad_out",
    group = 
"""
1  *1 C 1 {2,D}
2     O 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    label = "C_rad_out_single",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.328103,0.427434,0.500824,0.556541,0.634813,0.686808,0.76245,0.803032],"s^-1","*|/",[5.02379e+06,97889.5,9369.51,1990.64,298.259,99.8033,26.5873,15.7756])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [186, 186, 186, 186, 186, 186, 186, 186] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 167,
    label = "C_rad_out_2H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.835,2.90572,2.45697,2.19517,1.90395,1.74591,1.55122,1.45908],"s^-1","*|/",[2.46987e+08,1.79348e+06,94017.1,13234.9,1153.1,269.48,39.9771,15.915])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [41, 41, 41, 41, 41, 41, 41, 41] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 168,
    label = "C_rad_out_1H",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0369305,0.0849599,0.139089,0.192313,0.285979,0.36034,0.483173,0.553],"s^-1","*|/",[36124.8,2352.61,464.202,159.439,43.2259,20.4256,8.293,5.81866])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [62, 62, 62, 62, 62, 62, 62, 62] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 169,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.105936,0.184194,0.255054,0.315518,0.408528,0.473979,0.569988,0.618362],"s^-1","*|/",[40008.2,2558.09,499.836,170.75,46.0953,21.7816,8.89583,6.28112])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [55, 55, 55, 55, 55, 55, 55, 55] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 170,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.65239e-06,7.69895e-05,0.000574058,0.00217379,0.0113226,0.0301185,0.108228,0.20111],"s^-1","*|/",[483415,14655.4,1811.43,451.639,80.3276,28.7786,7.5514,4.03679])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 172,
    label = "C_rad_out_noH",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.310057,0.399718,0.469389,0.525337,0.610687,0.673968,0.782361,0.854732],"s^-1","*|/",[3.53998e+07,460128,34428.4,6179.77,739.72,212.393,43.3233,21.0783])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [74, 74, 74, 74, 74, 74, 74, 74] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 173,
    label = "C_rad_out_NonDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.538708,0.598649,0.643705,0.679779,0.735746,0.778694,0.856665,0.912632],"s^-1","*|/",[5.0999e+07,606679,43095,7478.28,859.461,241.141,47.8127,22.9605])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [70, 70, 70, 70, 70, 70, 70, 70] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 174,
    label = "C_rad_out_Cs2",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.538708,0.598649,0.643705,0.679779,0.735746,0.778694,0.856665,0.912632],"s^-1","*|/",[5.0999e+07,606679,43095,7478.28,859.461,241.141,47.8127,22.9605])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [70, 70, 70, 70, 70, 70, 70, 70] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 175,
    label = "C_rad_out_Cs2_cy3",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([84.8371,29.2995,15.2905,9.82972,5.57568,3.91876,2.38456,1.8216],"s^-1","*|/",[1423.03,186.799,54.9322,24.2286,8.70194,4.73458,2.23485,1.78263])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 176,
    label = "C_rad_out_Cs2_cy4",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.220396,0.256499,0.280143,0.296545,0.317337,0.329568,0.344515,0.350563],"s^-1","*|/",[1390.52,194.862,59.8412,27.2534,10.2555,5.77309,2.86133,2.23668])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 177,
    label = "C_rad_out_Cs2_cy5",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0828613,0.195662,0.329461,0.46802,0.730606,0.959706,1.39705,1.70133],"s^-1","*|/",[83224.7,19440.7,8963.22,5690.45,3567.79,2912.78,2568.25,2670.02])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 178,
    label = "Others-C_rad_out_Cs2",
    group = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.422464,0.488182,0.539519,0.581803,0.649441,0.702988,0.803728,0.878731],"s^-1","*|/",[7.49555e+08,4.37236e+06,200992,25917,2021.81,441.611,59.5433,22.4293])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [52, 52, 52, 52, 52, 52, 52, 52] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 179,
    label = "C_rad_out_NDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     O 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    label = "C_rad_out_OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.08944e-06,4.10869e-05,0.000357611,0.00149889,0.00883878,0.0252682,0.0994462,0.192613],"s^-1","*|/",[4.57088e+07,477355,29593.3,4499.02,404.305,90.8359,11.2154,3.6887])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 181,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.08944e-06,4.10869e-05,0.000357611,0.00149889,0.00883878,0.0252682,0.0994462,0.192613],"s^-1","*|/",[4.57088e+07,477355,29593.3,4499.02,404.305,90.8359,11.2154,3.6887])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 182,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    label = "C_rad_out_TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    label = "CO_H_out",
    group = 
"""
1  *2 CO 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    label = "O_H_out",
    group = 
"""
1  *2 O 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    label = "Ct_H_out",
    group = 
"""
1  *2 Ct 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    label = "Cb_H_out",
    group = 
"""
1  *2 Cb 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    label = "Cd_H_out_double",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     {Cd,O} 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.90825e-09,3.84739e-07,7.33957e-06,5.30122e-05,0.000640808,0.00290886,0.0226941,0.0652761],"s^-1","*|/",[3.62036e+10,6.41714e+07,1.47797e+06,122129,5619.29,916.06,88.208,29.3472])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 189,
    label = "Cd_H_out_doubleC",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.90825e-09,3.84739e-07,7.33957e-06,5.30122e-05,0.000640808,0.00290886,0.0226941,0.0652761],"s^-1","*|/",[3.62036e+10,6.41714e+07,1.47797e+06,122129,5619.29,916.06,88.208,29.3472])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=60 label="R4H_SDS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=189 label="Cd_H_out_doubleC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=189 label="Cd_H_out_doubleC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 190,
    label = "Cd_H_out_doubleO",
    group = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     O 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    label = "Cd_H_out_single",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.20069e-11,1.40926e-08,6.82109e-07,9.0732e-06,0.000231115,0.00161611,0.0217172,0.0799197],"s^-1","*|/",[6.79656e+12,3.55616e+09,3.80294e+07,1.84103e+06,41662.7,4284.92,207.177,46.0593])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [13, 13, 13, 13, 13, 13, 13, 13] rates.
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 192,
    label = "Cd_H_out_singleH",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.81125e-10,1.5436e-07,4.42587e-06,4.16459e-05,0.000691795,0.00375948,0.0364365,0.114717],"s^-1","*|/",[5.70243e+17,2.04351e+13,4.31393e+10,7.01419e+08,3.98943e+06,176494,2677.36,323.515])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=75 label="R5H_SSSD">, <Entry index=157 label="O_rad_out">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=100 label="R5H_SMSD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=192 label="Cd_H_out_singleH">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=192 label="Cd_H_out_singleH">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 193,
    label = "Cd_H_out_singleNd",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([9.18281e-12,8.96871e-09,5.53445e-07,8.59623e-06,0.000262543,0.00202594,0.0303648,0.11597],"s^-1","*|/",[6.68277e+11,3.73492e+08,4.22486e+06,214662,5261.98,577.475,31.7688,7.94306])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [5, 5, 5, 5, 5, 5, 5, 5] rates.
[<Entry index=26 label="R3H_SD">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=10 label="R2H_D">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=193 label="Cd_H_out_singleNd">]
[<Entry index=26 label="R3H_SD">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=193 label="Cd_H_out_singleNd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 194,
    label = "Cd_H_out_singleDe",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.53956e-20,2.10879e-15,1.37074e-12,1.04875e-10,2.45672e-08,6.68151e-07,5.81714e-05,0.000570152],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=26 label="R3H_SD">, <Entry index=167 label="C_rad_out_2H">, <Entry index=194 label="Cd_H_out_singleDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 195,
    label = "Cs_H_out",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.71032,3.15909,2.48436,2.11583,1.72987,1.53206,1.30142,1.19829],"s^-1","*|/",[559785,20281.9,2842.11,783.709,164.734,68.2499,24.5214,16.8419])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [241, 241, 241, 241, 241, 241, 241, 241] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 196,
    label = "Cs_H_out_2H",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.268488,0.406636,0.526277,0.62869,0.793424,0.920421,1.14331,1.29331],"s^-1","*|/",[8.07137e+06,145457,13393.4,2797.46,420.404,145.163,43.9822,29.9087])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [50, 50, 50, 50, 50, 50, 50, 50] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=95 label="R5H_DSMS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=60 label="R4H_SDS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=72 label="R5H_SSSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=74 label="R5H_SSSS_OOCs(Cs/Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=30 label="R3H_DS">, <Entry index=162 label="Cd_rad_out_singleDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
[<Entry index=73 label="R5H_SSSS_OOCs(Cs/Cs)">, <Entry index=157 label="O_rad_out">, <Entry index=196 label="Cs_H_out_2H">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 197,
    label = "Cs_H_out_1H",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.32963,2.18443,1.69988,1.44018,1.17354,1.04007,0.889418,0.825409],"s^-1","*|/",[7630.52,782.667,206.056,86.9836,31.5144,18.3088,10.5084,9.10272])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [107, 107, 107, 107, 107, 107, 107, 107] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=14 label="R3H_SS">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=5 label="R2H_S">, <Entry index=166 label="C_rad_out_single">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=197 label="Cs_H_out_1H">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 198,
    label = "Cs_H_out_H/NonDeC",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.0429,0.950815,0.901731,0.871849,0.838325,0.820852,0.80233,0.796517],"s^-1","*|/",[3697.52,453.896,130.732,57.6403,21.2014,11.9203,5.91304,4.43637])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [85, 85, 85, 85, 85, 85, 85, 85] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=37 label="R4H_SSS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=60 label="R4H_SDS">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=198 label="Cs_H_out_H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 199,
    label = "Cs_H_out_H/(NonDeC/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.367142,0.702751,1.04311,1.3622,1.91385,2.3597,3.156,3.68319],"s^-1","*|/",[15.2144,2.90475,2.2327,3.87527,9.98013,18.8936,48.9848,84.8795])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [3, 3, 3, 3, 3, 3, 3, 3] rates.
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=199 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 200,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.458274,0.840015,1.21161,1.54951,2.11411,2.55426,3.30595,3.77827],"s^-1","*|/",[59003.1,77.8267,1.84777,16.7477,744.297,8784.48,346005,2.92735e+06])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [2, 2, 2, 2, 2, 2, 2, 2] rates.
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=200 label="Cs_H_out_H/(NonDeC/Cs/Cs)">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 201,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S} {7,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.523111,0.919707,1.29574,1.63299,2.19149,2.62559,3.37132,3.84745],"s^-1")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [1, 1, 1, 1, 1, 1, 1, 1] rates.
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=201 label="Cs_H_out_H/(NonDeC/Cs/Cs/Cs)">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 202,
    label = "Cs_H_out_H/NonDeO",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([283.109,60.239,24.335,13.4951,6.62918,4.42415,2.70495,2.19513],"s^-1","*|/",[11269.2,1692.86,556.51,270.203,113.952,70.5586,40.9911,33.954])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=202 label="Cs_H_out_H/NonDeO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 203,
    label = "Cs_H_out_H/OneDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([255573,7896.1,986.92,247.822,44.4047,15.9343,4.12219,2.12056],"s^-1","*|/",[1.21932e+07,152570,11471.8,2120.94,281.987,93.5179,29.4189,21.7581])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [7, 7, 7, 7, 7, 7, 7, 7] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=203 label="Cs_H_out_H/OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=203 label="Cs_H_out_H/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 204,
    label = "Cs_H_out_noH",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([33.7072,15.0159,9.1609,6.55039,4.26141,3.26299,2.24224,1.83081],"s^-1","*|/",[1.26311e+07,218478,19627.3,4014.42,575.722,187.278,46.77,25.7763])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [84, 84, 84, 84, 84, 84, 84, 84] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=37 label="R4H_SSS">, <Entry index=166 label="C_rad_out_single">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=69 label="R5H_SSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=155 label="R7H">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=37 label="R4H_SSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=120 label="R6H_SSSSS">, <Entry index=157 label="O_rad_out">, <Entry index=204 label="Cs_H_out_noH">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 205,
    label = "Cs_H_out_NonDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([21.1848,10.881,7.23916,5.4886,3.84763,3.08505,2.26025,1.90958],"s^-1","*|/",[1.41471e+07,233473,20323.2,4059.57,562.084,178.033,42.3219,22.5062])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [75, 75, 75, 75, 75, 75, 75, 75] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 206,
    label = "Cs_H_out_Cs2",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15.6379,8.62494,5.98609,4.66699,3.38604,2.7703,2.08305,1.78157],"s^-1","*|/",[2.38448e+07,338341,26856.4,5038.73,643.726,193.971,43.0735,22.1717])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [69, 69, 69, 69, 69, 69, 69, 69] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 207,
    label = "Cs_H_out_Cs2_cy3",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([11364.6,960.83,221.155,83.8006,25.3099,12.5059,5.02642,3.25893],"s^-1","*|/",[5.22304e+32,3.16685e+24,3.80836e+19,2.03145e+16,1.69498e+12,6.20321e+09,3.68808e+06,93785.8])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=207 label="Cs_H_out_Cs2_cy3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 208,
    label = "Cs_H_out_Cs2_cy4",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([25.8703,11.1077,6.74153,4.85809,3.25589,2.58127,1.92634,1.68642],"s^-1","*|/",[317.31,72.0659,30.5338,17.5907,9.16635,6.38925,4.16663,3.4668])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=208 label="Cs_H_out_Cs2_cy4">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 209,
    label = "Cs_H_out_Cs2_cy5",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([283.159,57.5767,22.2412,11.8326,5.40539,3.39357,1.84216,1.3677],"s^-1","*|/",[964.7,148.953,50.7081,25.5497,11.5867,7.65653,4.98669,4.34368])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=209 label="Cs_H_out_Cs2_cy5">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 210,
    label = "Others-Cs_H_out_Cs2",
    group = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([5.04501,3.96363,3.38213,3.01471,2.56843,2.30081,1.92869,1.72505],"s^-1","*|/",[894.885,170.426,65.9467,36.3413,18.6351,13.389,9.93019,9.36271])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [51, 51, 51, 51, 51, 51, 51, 51] rates.
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=8 label="R2H_S_cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=15 label="R3H_SS_12cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=7 label="R2H_S_cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=171 label="C_rad_out_H/OneDe">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=19 label="R3H_SS_13cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=160 label="Cd_rad_out_singleH">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=177 label="C_rad_out_Cs2_cy5">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=16 label="R3H_SS_23cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=176 label="C_rad_out_Cs2_cy4">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=40 label="R4H_SSS_OO(Cs/Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S_cy3">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=23 label="R3H_SS_2Cd">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=38 label="R4H_SSS_OOCsCs">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=20 label="R3H_SS_12cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=18 label="R3H_SS_23cy4">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=25 label="Others-R3H_SS">, <Entry index=175 label="C_rad_out_Cs2_cy3">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=30 label="R3H_DS">, <Entry index=161 label="Cd_rad_out_singleNd">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=181 label="C_rad_out_OneDe/Cs">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=22 label="R3H_SS_13cy5">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=21 label="R3H_SS_23cy5">, <Entry index=167 label="C_rad_out_2H">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
[<Entry index=17 label="R3H_SS_12cy4">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=210 label="Others-Cs_H_out_Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 211,
    label = "Cs_H_out_NDMustO",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([10221.1,1231.9,346.515,148.874,51.8545,27.5719,11.9064,7.83933],"s^-1","*|/",[383149,28464.8,6283.97,2367.88,734.621,376.998,163.272,110.146])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [6, 6, 6, 6, 6, 6, 6, 6] rates.
[<Entry index=39 label="R4H_SSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=156 label="R7H_OOCs4">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=121 label="R6H_SSSSS_OO">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=70 label="R5H_SSSS_OOCCC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=24 label="R3H_SS_OC">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
[<Entry index=71 label="R5H_SSSS_OO(Cs/Cs)Cs">, <Entry index=157 label="O_rad_out">, <Entry index=211 label="Cs_H_out_NDMustO">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 212,
    label = "Cs_H_out_OneDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.93907e+06,38246.4,3567.14,725.513,97.1522,28.5935,5.40124,2.28237],"s^-1","*|/",[4.27925e+11,3.65172e+08,5.2476e+06,310075,9072,1101.49,70.311,19.7629])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to [4, 4, 4, 4, 4, 4, 4, 4] rates.
[<Entry index=9 label="Others-R2H_S">, <Entry index=178 label="Others-C_rad_out_Cs2">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=167 label="C_rad_out_2H">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=158 label="Cd_rad_out_double">, <Entry index=212 label="Cs_H_out_OneDe">]
[<Entry index=9 label="Others-R2H_S">, <Entry index=169 label="C_rad_out_H/NonDeC">, <Entry index=212 label="Cs_H_out_OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:21:55 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 213,
    label = "Cs_H_out_TwoDe",
    group = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: RnH
    L2: R2H
        L3: R2H_S
            L4: R2H_S_cy3
            L4: R2H_S_cy4
            L4: R2H_S_cy5
            L4: Others-R2H_S
        L3: R2H_D
        L3: R2H_B
    L2: R3H
        L3: R3H_SR
            L4: R3H_SS
                L5: R3H_SS_12cy3
                L5: R3H_SS_23cy3
                L5: R3H_SS_12cy4
                L5: R3H_SS_23cy4
                L5: R3H_SS_13cy4
                L5: R3H_SS_12cy5
                L5: R3H_SS_23cy5
                L5: R3H_SS_13cy5
                L5: R3H_SS_2Cd
                L5: R3H_SS_OC
                L5: Others-R3H_SS
            L4: R3H_SD
            L4: R3H_ST
            L4: R3H_SB
        L3: R3H_MS
            L4: R3H_DS
            L4: R3H_TS
            L4: R3H_BS
        L3: R3H_BB
    L2: R4H
        L3: R4H_RSR
            L4: R4H_RSS
                L5: R4H_SSS
                    L6: R4H_SSS_OOCsCs
                        L7: R4H_SSS_OO(Cs/Cs)Cs
                            L8: R4H_SSS_OO(Cs/Cs/Cs)Cs
                L5: R4H_DSS
                L5: R4H_TSS
                L5: R4H_BSS
            L4: R4H_RSD
                L5: R4H_SSD
                L5: R4H_DSD
                L5: R4H_TSD
                L5: R4H_BSD
            L4: R4H_RST
                L5: R4H_SST
                L5: R4H_DST
                L5: R4H_TST
                L5: R4H_BST
            L4: R4H_RSB
                L5: R4H_SSB
                L5: R4H_DSB
                L5: R4H_TSB
                L5: R4H_BSB
        L3: R4H_SMS
            L4: R4H_SDS
            L4: R4H_STS
            L4: R4H_SBS
        L3: R4H_SBB
        L3: R4H_BBS
        L3: R4H_BBB
    L2: R5H
        L3: R5H_RSSR
            L4: R5H_SSSR
                L5: R5H_SSSS
                    L6: R5H_SSSS_OOCCC
                        L7: R5H_SSSS_OO(Cs/Cs)Cs
                            L8: R5H_SSSS_OO(Cs/Cs/Cs)Cs
                        L7: R5H_SSSS_OOCs(Cs/Cs)
                            L8: R5H_SSSS_OOCs(Cs/Cs/Cs)
                L5: R5H_SSSD
                L5: R5H_SSST
                L5: R5H_SSSB
            L4: R5H_DSSR
                L5: R5H_DSSS
                L5: R5H_DSSD
                L5: R5H_DSST
                L5: R5H_DSSB
            L4: R5H_TSSR
                L5: R5H_TSSS
                L5: R5H_TSSD
                L5: R5H_TSST
                L5: R5H_TSSB
            L4: R5H_BSSR
                L5: R5H_BSSS
                L5: R5H_BSSD
                L5: R5H_BSST
                L5: R5H_BSSB
        L3: R5H_RSMS
            L4: R5H_SSMS
            L4: R5H_DSMS
            L4: R5H_TSMS
            L4: R5H_BSMS
        L3: R5H_SMSR
            L4: R5H_SMSS
            L4: R5H_SMSD
            L4: R5H_SMST
            L4: R5H_SMSB
        L3: R5H_BBSR
            L4: R5H_BBSS
            L4: R5H_BBSD
            L4: R5H_BBST
            L4: R5H_BBSB
        L3: R5H_RSBB
            L4: R5H_SSBB
            L4: R5H_DSBB
            L4: R5H_TSBB
            L4: R5H_BSBB
        L3: R5H_SBBS
        L3: R5H_SBBB
        L3: R5H_BBBS
        L3: R5H_BBBB
    L2: R6H
        L3: R6H_RSSSR
            L4: R6H_SSSSR
                L5: R6H_SSSSS
                    L6: R6H_SSSSS_OO
                L5: R6H_SSSSD
                L5: R6H_SSSST
                L5: R6H_SSSSB
            L4: R6H_DSSSR
                L5: R6H_DSSSS
                L5: R6H_DSSSD
                L5: R6H_DSSST
                L5: R6H_DSSSB
            L4: R6H_TSSSR
                L5: R6H_TSSSS
                L5: R6H_TSSSD
                L5: R6H_TSSST
                L5: R6H_TSSSB
            L4: R6H_BSSSR
                L5: R6H_BSSSS
                L5: R6H_BSSSD
                L5: R6H_BSSST
                L5: R6H_BSSSB
        L3: R6H_RSSMS
        L3: R6H_RSMSR
        L3: R6H_SMSSR
        L3: R6H_SMSMS
        L3: R6H_BBSRS
        L3: R6H_BBSSM
        L3: R6H_BBSBB
        L3: R6H_SBBSR
        L3: R6H_RSBBS
        L3: R6H_BBBSR
        L3: R6H_SBBBS
        L3: R6H_RSBBB
        L3: R6H_SBBBB
        L3: R6H_BBBBS
        L3: R6H_BBBBB
    L2: R7H
        L3: R7H_OOCs4
L1: Y_rad_out
    L2: O_rad_out
    L2: Cd_rad_out_double
    L2: Cd_rad_out_single
        L3: Cd_rad_out_singleH
        L3: Cd_rad_out_singleNd
        L3: Cd_rad_out_singleDe
    L2: Ct_rad_out
    L2: Cb_rad_out
    L2: CO_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                    L6: C_rad_out_Cs2_cy3
                    L6: C_rad_out_Cs2_cy4
                    L6: C_rad_out_Cs2_cy5
                    L6: Others-C_rad_out_Cs2
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
            L4: C_rad_out_TwoDe
L1: XH_out
    L2: CO_H_out
    L2: O_H_out
    L2: Ct_H_out
    L2: Cb_H_out
    L2: Cd_H_out_double
        L3: Cd_H_out_doubleC
        L3: Cd_H_out_doubleO
    L2: Cd_H_out_single
        L3: Cd_H_out_singleH
        L3: Cd_H_out_singleNd
        L3: Cd_H_out_singleDe
    L2: Cs_H_out
        L3: Cs_H_out_2H
        L3: Cs_H_out_1H
            L4: Cs_H_out_H/NonDeC
                L5: Cs_H_out_H/(NonDeC/Cs)
                    L6: Cs_H_out_H/(NonDeC/Cs/Cs)
                        L7: Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
            L4: Cs_H_out_H/NonDeO
            L4: Cs_H_out_H/OneDe
        L3: Cs_H_out_noH
            L4: Cs_H_out_NonDe
                L5: Cs_H_out_Cs2
                    L6: Cs_H_out_Cs2_cy3
                    L6: Cs_H_out_Cs2_cy4
                    L6: Cs_H_out_Cs2_cy5
                    L6: Others-Cs_H_out_Cs2
                L5: Cs_H_out_NDMustO
            L4: Cs_H_out_OneDe
            L4: Cs_H_out_TwoDe
"""
)

