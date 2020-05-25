#!/usr/bin/env python3

###############################################################################
#                                                                             #
# RMG - Reaction Mechanism Generator                                          #
#                                                                             #
# Copyright (c) 2002-2020 Prof. William H. Green (whgreen@mit.edu),           #
# Prof. Richard H. West (r.west@neu.edu) and the RMG Team (rmg_dev@mit.edu)   #
#                                                                             #
# Permission is hereby granted, free of charge, to any person obtaining a     #
# copy of this software and associated documentation files (the 'Software'),  #
# to deal in the Software without restriction, including without limitation   #
# the rights to use, copy, modify, merge, publish, distribute, sublicense,    #
# and/or sell copies of the Software, and to permit persons to whom the       #
# Software is furnished to do so, subject to the following conditions:        #
#                                                                             #
# The above copyright notice and this permission notice shall be included in  #
# all copies or substantial portions of the Software.                         #
#                                                                             #
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER         #
# DEALINGS IN THE SOFTWARE.                                                   #
#                                                                             #
###############################################################################

"""
This file provides atomic energy and BAC parameters for several model
chemistries.
"""

# Atom energy corrections to reach gas-phase reference state
# Experimental enthalpy of formation at 0 K, 1 bar for gas phase
# See Gaussian thermo whitepaper at http://gaussian.com/thermo/
# Note: These values are relatively old and some improvement may be possible by using newer values
# (particularly for carbon).
# However, care should be taken to ensure that they are compatible with the BAC values (if BACs are used)
# He, Ne, K, Ca, Ti, Cu, Zn, Ge, Br, Kr, Rb, Ag, Cd, Sn, I, Xe, Cs, Hg, and Pb are taken from CODATA
# Codata: Cox, J. D., Wagman, D. D., and Medvedev, V. A., CODATA Key Values for Thermodynamics, Hemisphere
# Publishing Corp., New York, 1989. (http://www.science.uwaterloo.ca/~cchieh/cact/tools/thermodata.html)

atom_hf = {'H': 51.63, 'He': -1.481,
           'Li': 37.69, 'Be': 76.48, 'B': 136.2, 'C': 169.98, 'N': 112.53, 'O': 58.99, 'F': 18.47, 'Ne': -1.481,
           'Na': 25.69, 'Mg': 34.87, 'Al': 78.23, 'Si': 106.6, 'P': 75.42, 'S': 65.66, 'Cl': 28.59,
           'K': 36.841, 'Ca': 41.014, 'Ti': 111.2, 'Cu': 79.16, 'Zn': 29.685, 'Ge': 87.1, 'Br': 25.26,
           'Kr': -1.481,
           'Rb': 17.86, 'Ag': 66.61, 'Cd': 25.240, 'Sn': 70.50, 'I': 24.04, 'Xe': -1.481,
           'Cs': 16.80, 'Hg': 13.19, 'Pb': 15.17}

# Thermal contribution to enthalpy for the atoms reported by Gaussian thermo whitepaper
# This will be subtracted from the corresponding value in atom_hf to produce an enthalpy used in calculating
# the enthalpy of formation at 298 K
atom_thermal = {'H': 1.01, 'He': 1.481,
                'Li': 1.1, 'Be': 0.46, 'B': 0.29, 'C': 0.25, 'N': 1.04, 'O': 1.04, 'F': 1.05, 'Ne': 1.481,
                'Na': 1.54, 'Mg': 1.19, 'Al': 1.08, 'Si': 0.76, 'P': 1.28, 'S': 1.05, 'Cl': 1.1,
                'K': 1.481, 'Ca': 1.481, 'Ti': 1.802, 'Cu': 1.481, 'Zn': 1.481, 'Ge': 1.768, 'Br': 1.481,
                'Kr': 1.481,
                'Rb': 1.481, 'Ag': 1.481, 'Cd': 1.481, 'Sn': 1.485, 'I': 1.481, 'Xe': 1.481,
                'Cs': 1.481, 'Hg': 1.481, 'Pb': 1.481}

# Spin orbit correction (SOC) in Hartrees
# Values taken from ref 22 of http://dx.doi.org/10.1063/1.477794 and converted to Hartrees
# Values in milli-Hartree are also available (with fewer significant figures) from table VII of
# http://dx.doi.org/10.1063/1.473182
# Iodine SOC calculated as a weighted average of the electronic spin splittings of the lowest energy state.
# The splittings are obtained from Huber, K.P.; Herzberg, G., Molecular Spectra and Molecular Structure. IV.
# Constants of Diatomic Molecules, Van Nostrand Reinhold Co., 1979
# Spin orbit correction for F, Si, Cl, Br and B taken form https://cccbdb.nist.gov/elecspin.asp
SOC = {'H': 0.0, 'N': 0.0, 'O': -0.000355, 'C': -0.000135, 'S': -0.000893, 'P': 0.0, 'I': -0.011547226,
       'F': -0.000614, 'Si': -0.000682, 'Cl': -0.001338, 'Br': -0.005597, 'B': -0.000046}

# Atomic energies
atom_energies = {
    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'H': -0.49338216995809725,
        'C': -37.84772407774059,
        'N': -54.59351384873174,
        'O': -75.0774947462408,
        'F': -99.74200231175924,
        'S': -398.0820818202818,
        'Cl': -460.1117669506163,
        'Br': -2573.9713149056824
    },

    # cbs-qb3 and cbs-qb3-paraskevas have the same corrections
    "LevelOfTheory(method='cbsqb3',software='gaussian')": {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },
    "LevelOfTheory(method='cbsqb3paraskevas',software='gaussian')": {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },

    "LevelOfTheory(method='m062x',basis='ccpvtz',software='gaussian')": {
        'H': -0.498135 + SOC['H'], 'N': -54.586780 + SOC['N'], 'O': -75.064242 + SOC['O'],
        'C': -37.842468 + SOC['C'], 'P': -341.246985 + SOC['P'], 'S': -398.101240 + SOC['S']
    },

    "LevelOfTheory(method='g3',software='gaussian')": {
        'H': -0.5010030, 'N': -54.564343, 'O': -75.030991, 'C': -37.827717, 'P': -341.116432, 'S': -397.961110
    },

    # * indicates that the grid size used in the [QChem] electronic
    # structure calculation utilized 75 radial points and 434 angular points
    # (i.e,, this is specified in the $rem section of the [qchem] input file as: XC_GRID 000075000434)
    "LevelOfTheory(method='m08so',basis='mg3s*',software='qchem')": {
        'H': -0.5017321350 + SOC['H'], 'N': -54.5574039365 + SOC['N'],
        'O': -75.0382931348 + SOC['O'], 'C': -37.8245648740 + SOC['C'],
        'P': -341.2444299005 + SOC['P'], 'S': -398.0940312227 + SOC['S']
    },

    "LevelOfTheory(method='klip_1')": {
        'H': -0.50003976 + SOC['H'], 'N': -54.53383153 + SOC['N'], 'O': -75.00935474 + SOC['O'],
        'C': -37.79266591 + SOC['C']
    },

    # Klip QCI(tz,qz)
    "LevelOfTheory(method='klip_2')": {
        'H': -0.50003976 + SOC['H'], 'N': -54.53169400 + SOC['N'], 'O': -75.00714902 + SOC['O'],
        'C': -37.79060419 + SOC['C']
    },

    # Klip QCI(dz,tz)
    "LevelOfTheory(method='klip_3')": {
        'H': -0.50005578 + SOC['H'], 'N': -54.53128140 + SOC['N'], 'O': -75.00356581 + SOC['O'],
        'C': -37.79025175 + SOC['C']
    },

    # Klip CCSD(T)(tz,qz)
    "LevelOfTheory(method='klip_2_cc')": {
        'H': -0.50003976 + SOC['H'], 'O': -75.00681155 + SOC['O'], 'C': -37.79029443 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_htz',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_hqz',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    # We are assuming that SOC is included in the Bond Energy Corrections
    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128, 'N': -54.526406291655, 'O': -74.995458316117,
        'C': -37.788203485235, 'S': -397.663040369707
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'H': -0.499946213243, 'N': -54.53000909621, 'O': -75.004127673424,
        'C': -37.789862146471, 'S': -397.675447487865
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',software='molpro')": {
        'H': -0.499994558325, 'N': -54.530515226371, 'O': -75.005600062003,
        'C': -37.789961656228, 'S': -397.676719774973
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.582137180344 + SOC['N'],
        'O': -75.053045547421 + SOC['O'], 'C': -37.840869118707 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.588545831900 + SOC['N'],
        'O': -75.065995072347 + SOC['O'], 'C': -37.844662139972 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvqzf12',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.589137594139 + SOC['N'],
        'O': -75.067412234737 + SOC['O'], 'C': -37.844893820561 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12(pp)',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.53000909621 + SOC['N'],
        'O': -75.004127673424 + SOC['O'], 'C': -37.789862146471 + SOC['C'],
        'S': -397.675447487865 + SOC['S'], 'I': -294.81781766 + SOC['I']
    },

    # ccsd(t)/aug-cc-pvtz(-pp) atomic energies were fit to a set of 8 small molecules:
    # CH4, CH3OH, H2S, H2O, SO2, HI, I2, CH3I
    "LevelOfTheory(method='ccsd(t)',basis='augccpvtz(pp)')": {
        'H': -0.499821176024 + SOC['H'], 'O': -74.96738492 + SOC['O'],
        'C': -37.77385697 + SOC['C'], 'S': -397.6461604 + SOC['S'],
        'I': -294.7958443 + SOC['I']
    },

    # note that all atom corrections but S are fitted, the correction for S is calculated
    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvdz',software='molpro')": {
        'H': -0.499459066131 + SOC['H'], 'N': -54.524279516472 + SOC['N'],
        'O': -74.992097308083 + SOC['O'], 'C': -37.786694171716 + SOC['C'],
        'S': -397.648733842400 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvtz',software='molpro')": {
        'H': -0.499844820798 + SOC['H'], 'N': -54.527419359906 + SOC['N'],
        'O': -75.000001429806 + SOC['O'], 'C': -37.788504810868 + SOC['C'],
        'S': -397.666903000231 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='augccpvqz',software='molpro')": {
        'H': -0.499949526073 + SOC['H'], 'N': -54.529569719016 + SOC['N'],
        'O': -75.004026586610 + SOC['O'], 'C': -37.789387892348 + SOC['C'],
        'S': -397.671214204994 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.523269942190 + SOC['N'],
        'O': -74.990725918500 + SOC['O'], 'C': -37.785409916465 + SOC['C'],
        'S': -397.658155086033 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.528135889213 + SOC['N'],
        'O': -75.001094055506 + SOC['O'], 'C': -37.788233578503 + SOC['C'],
        'S': -397.671745425929 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpvqzf12',software='molpro')": {
        'H': -0.499994558325 + SOC['H'], 'N': -54.529425753163 + SOC['N'],
        'O': -75.003820485005 + SOC['O'], 'C': -37.789006506290 + SOC['C'],
        'S': -397.674145126931 + SOC['S']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.578602780288 + SOC['N'],
        'O': -75.048064317367 + SOC['O'], 'C': -37.837592033417 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvtzf12',software='molpro')": {
        'H': -0.499946213243 + SOC['H'], 'N': -54.586402551258 + SOC['N'],
        'O': -75.062767632757 + SOC['O'], 'C': -37.842729156944 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='ccpcvqzf12',software='molpro')": {
        'H': -0.49999456 + SOC['H'], 'N': -54.587781507581 + SOC['N'],
        'O': -75.065397706471 + SOC['O'], 'C': -37.843634971592 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvdz',software='molpro')": {
        'H': -0.499459066131 + SOC['H'], 'N': -54.520475581942 + SOC['N'],
        'O': -74.986992215049 + SOC['O'], 'C': -37.783294495799 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvtz',software='molpro')": {
        'H': -0.499844820798 + SOC['H'], 'N': -54.524927371700 + SOC['N'],
        'O': -74.996328829705 + SOC['O'], 'C': -37.786320700792 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12b',basis='augccpvqz',software='molpro')": {
        'H': -0.499949526073 + SOC['H'], 'N': -54.528189769291 + SOC['N'],
        'O': -75.001879610563 + SOC['O'], 'C': -37.788165047059 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvdz')": {
        'H': -0.49927840 + SOC['H'], 'N': -54.46141996 + SOC['N'], 'O': -74.89408254 + SOC['O'],
        'C': -37.73792713 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvtz')": {
        'H': -0.49980981 + SOC['H'], 'N': -54.49615972 + SOC['N'], 'O': -74.95506980 + SOC['O'],
        'C': -37.75833104 + SOC['C']
    },

    "LevelOfTheory(method='mp2',basis='ccpvqz')": {
        'H': -0.49994557 + SOC['H'], 'N': -54.50715868 + SOC['N'], 'O': -74.97515364 + SOC['O'],
        'C': -37.76533215 + SOC['C']
    },

    "LevelOfTheory(method='ccsdf12',basis='ccpvdzf12',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.524325513811 + SOC['N'],
        'O': -74.992326577897 + SOC['O'], 'C': -37.786213495943 + SOC['C']
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12_noscale',software='molpro')": {
        'H': -0.499811124128 + SOC['H'], 'N': -54.526026290887 + SOC['N'],
        'O': -74.994751897699 + SOC['O'], 'C': -37.787881871511 + SOC['C']
    },

    "LevelOfTheory(method='pbepbe',basis='6311++g(d,p)',software='gaussian')": {
        'H': -0.499812273282 + SOC['H'], 'N': -54.5289567564 + SOC['N'],
        'O': -75.0033596764 + SOC['O'], 'C': -37.7937388736 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvdz')": {
        'C': -37.789527 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvtz')": {
        'C': -37.781266669684 + SOC['C']
    },

    "LevelOfTheory(method='fci',basis='ccpvqz')": {
        'C': -37.787052110598 + SOC['C']
    },

    # 'bmk/cbsb7' and 'bmk/6-311g(2d,d,p)' have the same corrections
    "LevelOfTheory(method='bmk',basis='cbsb7',software='gaussian')": {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },
    "LevelOfTheory(method='bmk',basis='6311g(2d,d,p)',software='gaussian')": {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },

    # Fitted to small molecules
    "LevelOfTheory(method='b3lyp',basis='631g(d,p)',software='gaussian')": {
        'H': -0.500426155, 'C': -37.850331697831, 'O': -75.0535872748806, 'S': -398.100820107242
    },

    # Calculated atomic energies
    "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)',software='gaussian')": {
        'H': -0.502155915123 + SOC['H'], 'C': -37.8574709934 + SOC['C'],
        'N': -54.6007233609 + SOC['N'], 'O': -75.0909131284 + SOC['O'],
        'P': -341.281730319 + SOC['P'], 'S': -398.134489850 + SOC['S']
    },

    "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": {
        'H': -0.502803 + SOC['H'], 'N': -54.585652 + SOC['N'], 'O': -75.068286 + SOC['O'],
        'C': -37.842014 + SOC['C']
    },

    # Calculated atomic energies (unfitted)
    "LevelOfTheory(method='mrci+davidson',basis='augccpv(t+d)z',software='molpro')": {
        'H': -0.49982118 + SOC['H'], 'C': -37.78321274 + SOC['C'], 'N': -54.51729444 + SOC['N'],
        'O': -74.97847534 + SOC['O'], 'S': -397.6571654 + SOC['S']
    },

}

# Petersson-type bond additivity correction parameters
pbac = {

    "LevelOfTheory(method='b3lypd3bj',basis='def2tzvp',software='gaussian')": {
        'Br-Br': 0.5185156767091978,
        'Br-C': -0.9577504278588156,
        'Br-Cl': 0.775822683599642,
        'Br-H': 0.4572616416556361,
        'Br-O': 0.2043742691865884,
        'C#C': -5.38720460824316,
        'C#N': -1.4697566930299064,
        'C#O': -8.37401091882317,
        'C-C': -2.7695071290444933,
        'C-Cl': -0.9774345169996838,
        'C-H': 0.05806248235595328,
        'C-N': -0.7840938182617309,
        'C-O': -2.2116962927406383,
        'C-S': -2.4737081990029157,
        'C=C': -2.443173148719635,
        'C=N': -0.8239045314834288,
        'C=O': -2.2192234101953763,
        'C=S': -2.0285045935931953,
        'Cl-Cl': 1.0785419856630345,
        'Cl-H': 0.04915737799971254,
        'Cl-N': 3.7499799567518544,
        'Cl-O': 0.763405809596614,
        'Cl-S': 0.27732415760384654,
        'H-H': 1.909833906261407,
        'H-N': 0.976608941059378,
        'H-O': -1.567801028736581,
        'H-S': 0.5700725801878385,
        'N#N': -1.9800094030561088,
        'N-N': 3.2062861973173673,
        'N-O': 1.3853348209888028,
        'N=N': 3.7974680237792295,
        'N=O': -0.33242521937722463,
        'O-O': 0.3248931710140498,
        'O-S': -3.2896810976569797,
        'O=O': -8.92878449794968,
        'O=S': -4.456237634540539,
        'S-S': -0.5198234606383603,
        'S=S': -3.7746270990364343
    },

    "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": {
        'Br-Br': 0.016045619067636352,
        'Br-C': -1.0401173711203133,
        'Br-Cl': 0.2983927031966531,
        'Br-H': 0.9415811759953474,
        'Br-O': -1.5611232414179237,
        'C#C': -7.22638483094488,
        'C#N': -3.025697788832491,
        'C#O': -7.031708654318713,
        'C-C': -1.2939356753685136,
        'C-Cl': -0.9496033384719503,
        'C-H': 0.18748207622260252,
        'C-N': 0.33806423908535604,
        'C-O': -1.4847965500532676,
        'C-S': -1.680227500725586,
        'C=C': -3.2447299874715707,
        'C=N': -0.935406901068859,
        'C=O': -2.3043966309101966,
        'C=S': -3.4749183307650258,
        'Cl-Cl': 0.39648213676177524,
        'Cl-H': 0.10677101518796661,
        'Cl-N': 0.953874070689174,
        'Cl-O': -1.3793439739818782,
        'Cl-S': -0.5348211607370006,
        'H-H': 0.22480639824807758,
        'H-N': 1.038629931847478,
        'H-O': -1.0042110205565615,
        'H-S': 0.9630019170637759,
        'N#N': -0.780153706091782,
        'N-N': 3.62665588475469,
        'N-O': 0.7831718131424773,
        'N=N': 2.6853663579609024,
        'N=O': -0.849094503813265,
        'O-O': -1.5235846478681454,
        'O-S': -3.2453957184035045,
        'O=O': -9.953519761276839,
        'O=S': -3.4945349305218114,
        'S-S': -1.3155402429488239,
        'S=S': -5.848810185696702
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'Br-Br': 0.1958610046250353,
        'Br-C': 0.08342615830647254,
        'Br-Cl': 0.15262164580006665,
        'Br-F': 1.554766957397149,
        'Br-H': 0.5081557501289318,
        'Br-O': -1.2236043316175111,
        'C#C': -2.6349164523184414,
        'C#N': -1.1906643794269727,
        'C#O': -1.2169066048908732,
        'C-C': -0.05280224931801543,
        'C-Cl': 0.09412550983382971,
        'C-F': 1.657136384442864,
        'C-H': -0.01586761480957165,
        'C-N': 0.8464785445254364,
        'C-O': -0.022295634798634844,
        'C-S': -0.1201537369814494,
        'C=C': -0.8020718163585956,
        'C=N': -0.23249839836435446,
        'C=O': -0.6923581569910078,
        'C=S': -1.4039224541066722,
        'Cl-Cl': 0.24706245542077263,
        'Cl-F': 1.5870013888348105,
        'Cl-H': -0.061538610443722774,
        'Cl-N': 0.9215949633998766,
        'Cl-O': -0.10690598725501184,
        'Cl-S': -0.26928317951073,
        'F-F': 0.7076947926501269,
        'F-H': -0.7608076549745562,
        'F-O': 0.6414896651183406,
        'F-S': 1.0255233686038518,
        'H-H': -0.4548842455328711,
        'H-N': 0.32770189779757325,
        'H-O': -0.3482010477866195,
        'H-S': 1.0420963399199659,
        'N#N': 0.446870060585342,
        'N-N': 2.4305267415020237,
        'N-O': 1.0847843547592344,
        'N=N': 1.2304781903332842,
        'N=O': -2.379892376833476,
        'O-O': -0.8522025877305646,
        'O-S': -1.3007885702567272,
        'O=O': -9.628885866255034,
        'O=S': -2.1776302846961637,
        'S-S': 0.14292519243155768,
        'S=S': -3.3100912737119246
    },

    # 'S-H', 'C-S', 'C=S', 'S-S', 'O-S', 'O=S', 'O=S=O' taken from http://hdl.handle.net/1721.1/98155 (both for
    # 'CCSD(T)-F12/cc-pVDZ-F12' and 'CCSD(T)-F12/cc-pVTZ-F12')
    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro')": {
        'C-H': -0.46, 'C-C': -0.68, 'C=C': -1.90, 'C#C': -3.13,
        'O-H': -0.51, 'C-O': -0.23, 'C=O': -0.69, 'O-O': -0.02, 'C-N': -0.67,
        'C=N': -1.46, 'C#N': -2.79, 'N-O': 0.74, 'N_O': -0.23, 'N=O': -0.51,
        'N-H': -0.69, 'N-N': -0.47, 'N=N': -1.54, 'N#N': -2.05, 'S-H': 0.87,
        'C-S': 0.42, 'C=S': 0.51, 'S-S': 0.86, 'O-S': 0.23, 'O=S': -0.53,
        'O=S=O': 1.95
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'C-H': -0.09, 'C-C': -0.27, 'C=C': -1.03, 'C#C': -1.79,
        'O-H': -0.06, 'C-O': 0.14, 'C=O': -0.19, 'O-O': 0.16, 'C-N': -0.18,
        'C=N': -0.41, 'C#N': -1.41, 'N-O': 0.87, 'N_O': -0.09, 'N=O': -0.23,
        'N-H': -0.01, 'N-N': -0.21, 'N=N': -0.44, 'N#N': -0.76, 'S-H': 0.52,
        'C-S': 0.13, 'C=S': -0.12, 'S-S': 0.30, 'O-S': 0.15, 'O=S': -2.61,
        'O=S=O': 0.27
    },

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',software='molpro')": {
        'C-H': -0.08, 'C-C': -0.26, 'C=C': -1.01, 'C#C': -1.66,
        'O-H': 0.07, 'C-O': 0.25, 'C=O': -0.03, 'O-O': 0.26, 'C-N': -0.20,
        'C=N': -0.30, 'C#N': -1.33, 'N-O': 1.01, 'N_O': -0.03, 'N=O': -0.26,
        'N-H': 0.06, 'N-N': -0.23, 'N=N': -0.37, 'N#N': -0.64
    },

    "LevelOfTheory(method='cbsqb3',software='gaussian')": {
        'C-H': -0.11, 'C-C': -0.30, 'C=C': -0.08, 'C#C': -0.64, 'O-H': 0.02, 'C-O': 0.33, 'C=O': 0.55,
        # Table IX: Petersson GA (1998) J. of Chemical Physics, DOI: 10.1063/1.477794
        'N-H': -0.42, 'C-N': -0.13, 'C#N': -0.89, 'C-F': 0.55, 'C-Cl': 1.29, 'S-H': 0.0, 'C-S': 0.43,
        'O=S': -0.78,
        'N=O': 1.11, 'N-N': -1.87, 'N=N': -1.58, 'N-O': 0.35,
        # Table 2: Ashcraft R (2007) J. Phys. Chem. B; DOI: 10.1021/jp073539t
        'N#N': -2.0, 'O=O': -0.2, 'H-H': 1.1,  # Unknown source
    },

    "LevelOfTheory(method='cbsqb3paraskevas',software='gaussian')": {
        # NOTE: The Paraskevas corrections are inaccurate for non-oxygenated hydrocarbons,
        # and may do poorly in combination with the Petersson corrections
        'C-C': -0.495, 'C-H': -0.045, 'C=C': -0.825, 'C-O': 0.378, 'C=O': 0.743, 'O-H': -0.423,
        # Table2: Paraskevas, PD (2013). Chemistry-A European J., DOI: 10.1002/chem.201301381
        'C#C': -0.64, 'C#N': -0.89, 'C-S': 0.43, 'O=S': -0.78, 'S-H': 0.0, 'C-N': -0.13, 'C-Cl': 1.29,
        'C-F': 0.55,  # Table IX: Petersson GA (1998) J. of Chemical Physics, DOI: 10.1063/1.477794
        'N-H': -0.42, 'N=O': 1.11, 'N-N': -1.87, 'N=N': -1.58, 'N-O': 0.35,
        # Table 2: Ashcraft R (2007) J. Phys. Chem. B; DOI: 10.1021/jp073539t
        'N#N': -2.0, 'O=O': -0.2, 'H-H': 1.1,  # Unknown source
    },

    # Identical corrections for 'b3lyp/cbsb7', 'b3lyp/6-311g(2d,d,p)', 'b3lyp/6-311+g(3df,2p)', 'b3lyp/6-31g(d,p)'
    "LevelOfTheory(method='b3lyp',basis='cbsb7',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='6311g(2d,d,p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    "LevelOfTheory(method='b3lyp',basis='631g(d,p)',software='gaussian')": {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },

}

# Melius-type bond additivity correction parameters
mbac = {

    "LevelOfTheory(method='b3lypd3bj',basis='def2tzvp',software='gaussian')": {
        'atom_corr': {
            'Br': -2.871729911568782,
            'C': -1.3419167625995925,
            'Cl': -2.9651214556544656,
            'H': -3.114980999128395,
            'N': -4.924326298384489,
            'O': -4.999999999999999,
            'S': -3.3925874022291898
        },
        'bond_corr_length': {
            'Br': 2631.9637073123527,
            'C': 63.738365607463365,
            'Cl': 581.2291799334001,
            'H': 19.208130319016973,
            'N': 23.89697799951957,
            'O': 260.0614872024786,
            'S': 792.781184185199
        },
        'bond_corr_neighbor': {
            'Br': 0.22065107274594775,
            'C': 0.09705844364422887,
            'Cl': 0.3473967982906402,
            'H': 0.0061635645102511944,
            'N': -0.10776324055195008,
            'O': 0.1445617604626904,
            'S': 0.11500345710920869
        },
        'mol_corr': -2.5980867963328214
    },

    "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": {
        'atom_corr': {
            'Br': -3.500404614452807,
            'C': 0.6043384108781988,
            'Cl': -2.2199867323856046,
            'H': -2.697298969939275,
            'N': -4.813583567105453,
            'O': -3.705141560518769,
            'S': -2.0470365288143086
        },
        'bond_corr_length': {
            'Br': 3855.3219992167105,
            'C': 5.265929765122098,
            'Cl': 395.15445737554194,
            'H': 7.004552459950368,
            'N': 5.842909193095168,
            'O': 193.62341632004774,
            'S': 346.55692844813734
        },
        'bond_corr_neighbor': {
            'Br': 0.7022794185349223,
            'C': -0.0675116935249027,
            'Cl': 0.2542743481491643,
            'H': 0.049067908864623394,
            'N': -0.24464250898424794,
            'O': 0.15899890845973066,
            'S': -0.02495699084856554
        },
        'mol_corr': -3.045051588951062
    },

    "LevelOfTheory(method='wb97mv',basis='def2tzvpd',software='qchem')": {
        'atom_corr': {
            'Br': -1.2684797610740068,
            'C': -0.4174257352393245,
            'Cl': -0.9661365064678925,
            'F': -2.7269618018691286,
            'H': -0.8200512641588867,
            'N': -1.9268795831605057,
            'O': -1.2065799989531332,
            'S': -1.4981603387204314
        },
        'bond_corr_length': {
            'Br': 1080.374675861722,
            'C': 0.9866591151048302,
            'Cl': 14.168290439224558,
            'F': 53.677336144261815,
            'H': 0.10560986920930937,
            'N': 7.102031391504367,
            'O': 116.712690311844,
            'S': 282.9043317540571
        },
        'bond_corr_neighbor': {
            'Br': 0.0646368151807638,
            'C': -0.04831303352995286,
            'Cl': 0.014147411281693778,
            'F': 0.05343762573411219,
            'H': 0.011152914014086364,
            'N': -0.23350242741116362,
            'O': -0.10294376619330678,
            'S': -0.07865422498372374
        },
        'mol_corr': -1.4470179217148968
    },

}


# Frequency scale factors
#    Refer to https://comp.chem.umn.edu/freqscale/index.html for future updates of these factors
#
#    Sources:
#        [1] I.M. Alecu, J. Zheng, Y. Zhao, D.G. Truhlar, J. Chem. Theory Comput. 2010, 6, 2872, DOI: 10.1021/ct100326h
#        [2] http://cccbdb.nist.gov/vibscalejust.asp
#        [3] http://comp.chem.umn.edu/freqscale/190107_Database_of_Freq_Scale_Factors_v4.pdf
#        [4] Calculated as described in 10.1021/ct100326h
#        [5] J.A. Montgomery, M.J. Frisch, J. Chem. Phys. 1999, 110, 2822–2827, DOI: 10.1063/1.477924

freq_dict = {"LevelOfTheory(method='hf',basis='sto3g')": 0.817,  # [2]
             "LevelOfTheory(method='hf',basis='631g')": 0.903,  # [2]
             "LevelOfTheory(method='hf',basis='631g(d)')": 0.899,  # [2]
             "LevelOfTheory(method='hf',basis='631g(d,p)')": 0.903,  # [2]
             "LevelOfTheory(method='hf',basis='631g+(d,p)')": 0.904,  # [2]
             "LevelOfTheory(method='hf',basis='631+g(d,p)')": 0.915 * 1.014,  # [1] Table 7
             "LevelOfTheory(method='pm3')": 0.940 * 1.014,  # [1] Table 7, the 0.940 value is the ZPE scale factor
             "LevelOfTheory(method='pm6')": 1.078 * 1.014,  # [1] Table 7, the 1.078 value is the ZPE scale factor
             "LevelOfTheory(method='b3lyp',basis='631g(d,p)')": 0.961,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311g(d,p)')": 0.967,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2p)')": 0.967,  # [2]
             "LevelOfTheory(method='b3lyp',basis='6311+g(3df,2pd)')": 0.970,  # [2]
             "LevelOfTheory(method='b3lyp-d3bj',basis='def2-tzvp')": 0.999,  # [4]
             "LevelOfTheory(method='m062x',basis='631g(d,p)')": 0.952,  # [2]
             "LevelOfTheory(method='m062x',basis='631+g(d,p)')": 0.979,  # [3]
             "LevelOfTheory(method='m062x',basis='6311+g(d,p)')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='6311++g(d,p)')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='ccpvtz')": 0.955,  # [2]
             "LevelOfTheory(method='m062x',basis='augccpvdz')": 0.993,  # [3]
             "LevelOfTheory(method='m062x',basis='augccpvtz')": 0.985,  # [1] Table 3, [3]
             "LevelOfTheory(method='m062x',basis='def2tzvp')": 0.984,  # [3]
             "LevelOfTheory(method='m062x',basis='def2qzvp')": 0.983,  # [3]
             "LevelOfTheory(method='m062x',basis='def2tzvpp')": 0.983,  # [1] Table 3, [3]
             "LevelOfTheory(method='m08so',basis='mg3s*')": 0.995,  # [1] Table 3, taken as 'M08-SO/MG3S'
             "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": 0.988,  # [3], taken as 'ωB97X-D/maug-cc-pVTZ'
             "LevelOfTheory(method='wb97xd',basis='6311++g(d,p)',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian')": 0.986,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvp')": 1.001,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvpd')": 1.002,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvp')": 0.993,  # [4]
             "LevelOfTheory(method='apfd',basis='def2tzvpp')": 0.992,  # [4]
             "LevelOfTheory(method='mp2',basis='ccpvdz')": 0.953,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvtz')": 0.950,  # [2]
             "LevelOfTheory(method='mp2',basis='ccpvqz')": 0.962,  # [2]
             "LevelOfTheory(method='cbsqb3')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='cbsqb3paraskevas')": 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             "LevelOfTheory(method='ccsdf12',basis='ccpvdzf12')": 0.947,  # [2], taken as 'CCSD/cc-pVDZ'
             "LevelOfTheory(method='ccsd(t)',basis='ccpvdz')": 0.979,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpvtz')": 0.975,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpvqz')": 0.970,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvdz')": 0.963,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvtz')": 1.001,  # [3]
             "LevelOfTheory(method='ccsd(t)',basis='augccpvqz')": 0.975,  # [2]
             "LevelOfTheory(method='ccsd(t)',basis='ccpv(t+d)z')": 0.965,  # [2]
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12')": 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12')": 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpvqzf12',)": 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvdzf12')": 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='ccpcvtzf12')": 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvdz')": 0.997,  # [3], taken as 'CCSD(T)/cc-pVDZ'
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvtz')": 0.998,  # [3], taken as CCSD(T)-F12a/cc-pVTZ-F12
             "LevelOfTheory(method='ccsd(t)f12',basis='augccpvqz')": 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             }
