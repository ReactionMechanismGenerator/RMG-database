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


    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'H': -0.49991749801833063,
        'C': -37.84993993601866,
        'N': -54.58750889521559,
        'O': -75.07402423801669,
        'F': -99.7392410428872,
        'S': -398.10051734579775,
        'Cl': -460.1341841971797,
        'Br': -2574.175384284091
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'H': -0.49516021903680546,
        'C': -37.833878658169624,
        'N': -54.541699219144505,
        'O': -75.01524900146931,
        'F': -99.65948092488345,
        'S': -397.97912317555034,
        'Cl': -459.9963616463421,
        'Br': -2575.1192984500663
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
	    'H': -0.50000836574607,
	    'C': -37.784271457731904,
	    'N': -54.523156256858144,
	    'O': -74.99320041804718,
	    'F': -99.6511861642652,
	    'S': -397.6625539051389,
	    'Cl': -459.68886861844055
	},

    "LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro')": {
        'H': -0.5003554055415579,
        'C': -37.787690380768844,
        'N': -54.52874573314225,
        'O': -75.00314974528959,
        'F': -99.6658140570029,
        'S': -397.67549377693314,
        'Cl': -459.70521576925796
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

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro'))": {
        'C#C': -0.37319831366523176,
        'C#N': -0.04394537008104246,
        'C#O': 0.6845507542289013,
        'C-C': 0.12602185168066687,
        'C-Cl': 0.4000395071268901,
        'C-F': 0.5386953055500939,
        'C-H': 0.03014784912580578,
        'C-N': 0.3022567343857892,
        'C-O': 0.22156464774957604,
        'C-S': 0.059041022372472614,
        'C=C': -0.049584091100670837,
        'C=N': -0.4428639989215071,
        'C=O': 0.05943900637676746,
        'C=S': -0.7758177193710785,
        'Cl-Cl': 0.1382704625282193,
        'Cl-F': 0.3846791604086004,
        'Cl-H': 0.19401601074149966,
        'Cl-N': 0.4109773959959559,
        'Cl-O': 0.2892748705965537,
        'Cl-S': 0.21784097251125079,
        'F-F': -0.6423018409407416,
        'F-H': 0.1102321131699,
        'F-O': -0.5555283888816168,
        'F-S': 0.8514568108157713,
        'H-H': -0.24061025875957348,
        'H-N': -0.2458184828878194,
        'H-O': 0.007966375791966561,
        'H-S': 0.6141296238226581,
        'N#N': 0.15991986841815756,
        'N-N': 1.2279613861249787,
        'N-O': 0.20879882425699858,
        'N=N': 0.44949205775999634,
        'N=O': -1.029059282226874,
        'O-O': -0.611163660061622,
        'O-S': -0.43698174359431335,
        'O=O': -2.8858691436809196,
        'O=S': 0.3100869947699715,
        'S-S': 0.10571953923531874,
        'S=S': -1.6070546530751422
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro'))": {
        'C#C': -0.7940736288861328,
        'C#N': -0.2736082180869344,
        'C#O': 1.215648303725274,
        'C-C': -0.006153161261658441,
        'C-Cl': 0.7595723077901367,
        'C-F': 0.4815204101380463,
        'C-H': 0.010156098370800108,
        'C-N': 0.10438905540134882,
        'C-O': 0.09987252247930076,
        'C-S': 0.4090396417072708,
        'C=C': -0.32837634513571645,
        'C=N': -0.6872690836499937,
        'C=O': -0.011879042720396643,
        'C=S': -0.45740929709171363,
        'Cl-Cl': -0.014451326911147977,
        'Cl-F': 0.6479093120532244,
        'Cl-H': 0.37650914650193457,
        'Cl-N': 0.5872703379266317,
        'Cl-O': 0.5095510277409292,
        'Cl-S': 0.646585596795355,
        'F-F': -0.7037812030852666,
        'F-H': 0.13879622147405257,
        'F-O': -0.5823379151756342,
        'F-S': 0.9474443582208304,
        'H-H': -0.00879296155638677,
        'H-N': -0.3973581320058072,
        'H-O': -0.05082328074118156,
        'H-S': 0.9006352849672502,
        'N#N': 0.6426432154389473,
        'N-N': 1.0261474051290596,
        'N-O': -0.03642922490749102,
        'N=N': 0.1708502331465831,
        'N=O': -0.8042125954300557,
        'O-O': -0.7325577965540944,
        'O-S': -0.18825122982916948,
        'O=O': -2.7021030234346695,
        'O=S': 0.9232025676598207,
        'S-S': 0.14102013117456597,
        'S=S': -0.9855656265939845
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'Br-Br': 3.3184897418778894,
        'Br-C': -0.6447457118766096,
        'Br-Cl': 2.5458979359916487,
        'Br-F': 3.9321266497717513,
        'Br-H': 3.1450731163630294,
        'Br-O': -7.328960869354291,
        'C#C': -19.75782127331025,
        'C#N': -7.499027151749764,
        'C#O': -18.475225675145023,
        'C-C': -6.498460645920902,
        'C-Cl': -1.9238440096546874,
        'C-F': -1.9747353079897023,
        'C-H': 0.01729290032079855,
        'C-N': -1.7433898062480928,
        'C-O': -3.8525377364775215,
        'C-S': -5.419539134610862,
        'C=C': -12.998063133432941,
        'C=N': -5.027572638791928,
        'C=O': -6.801076987753849,
        'C=S': -5.654222632762431,
        'Cl-Cl': 1.3452682321784095,
        'Cl-F': 3.491738723755338,
        'Cl-H': 0.8075310212109841,
        'Cl-N': 11.423744786147633,
        'Cl-O': 5.488334623555848,
        'Cl-S': -3.0170592756249057,
        'F-F': 5.002957678305598,
        'F-H': -8.586384858108858,
        'F-O': 4.485916714230829,
        'F-S': -4.159578702518104,
        'H-H': 8.526122583518188,
        'H-N': 1.2169107867656828,
        'H-O': -3.8567427899343043,
        'H-S': 1.8235600781274208,
        'N#N': 2.7964223466789293,
        'N-N': 5.170147621733188,
        'N-O': 3.5592924696925587,
        'N=N': 8.731292427600357,
        'N=O': 5.09080676349987,
        'O-O': 2.565372397566582,
        'O-S': -8.578422244244877,
        'O=O': 1.3114212140745158,
        'O=S': -14.229024507889747,
        'S-S': -4.258008825508542,
        'S=S': -3.631460853989999
    },

    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'Br-Br': 2.849979178650586,
        'Br-C': 0.7381762723415655,
        'Br-Cl': 1.4764289266543953,
        'Br-F': 2.7336108440861704,
        'Br-H': 2.621866526877559,
        'Br-O': -2.5532834764130006,
        'C#C': -7.92496166307853,
        'C#N': -3.864663093893819,
        'C#O': -7.484067031104203,
        'C-C': -1.0817871087375186,
        'C-Cl': -0.5732704243120552,
        'C-F': 1.3719540592946495,
        'C-H': 0.07704003746021679,
        'C-N': 0.5919032459443995,
        'C-O': -1.2626115105817743,
        'C-S': -1.2805399168193157,
        'C=C': -3.890848609981227,
        'C=N': -1.5036825315665,
        'C=O': -2.9505302757552596,
        'C=S': -3.7136643912288623,
        'Cl-Cl': 0.136962629607007,
        'Cl-F': 1.043801519750975,
        'Cl-H': 0.3209061926667829,
        'Cl-N': 1.254243872961764,
        'Cl-O': -1.2050377287736824,
        'Cl-S': -0.353190509282856,
        'F-F': 1.2363169265407195,
        'F-H': -1.4703521420571022,
        'F-O': -0.008583994665357622,
        'F-S': 0.3093056813192921,
        'H-H': 0.16749830148486178,
        'H-N': 0.7806156486742294,
        'H-O': -1.2446586747155781,
        'H-S': 1.186472823080999,
        'N#N': -0.15105524935670453,
        'N-N': 3.437416216021716,
        'N-O': 1.4467328418363092,
        'N=N': 2.786466016509395,
        'N=O': -2.389849264267907,
        'O-O': -2.27124059610634,
        'O-S': -2.6554640707366945,
        'O=O': -9.840434624890442,
        'O=S': -3.470457647257026,
        'S-S': -1.3273180651577856,
        'S=S': -6.864453512935457
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

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvtzf12',software='molpro'))": {
        'atom_corr': {
            'C': -0.6004599146970828,
            'Cl': -0.21285368087888518,
            'F': 0.20136534958427602,
            'H': 0.1409606206795142,
            'N': 0.44677472396061857,
            'O': 0.7724579645053421,
            'S': -0.1294113249415446
        },
        'bond_corr_length': {
            'C': 57.600230521006345,
            'Cl': 72.75494140267224,
            'F': 2.7637442704545506e-39,
            'H': 0.04568584404132764,
            'N': 7.988043181948807,
            'O': 1.1170405486633287e-25,
            'S': 337.25420543898184
        },
        'bond_corr_neighbor': {
            'C': -0.02675767045779017,
            'Cl': -0.026157341196276294,
            'F': -0.09738287356772249,
            'H': 0.08331791884967885,
            'N': -0.031799354286893795,
            'O': -0.04321158886089615,
            'S': -0.07172725215109269
        },
        'mol_corr': 0.3057912044551125
    },

    "CompositeLevelOfTheory(freq=LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem'),energy=LevelOfTheory(method='ccsd(t)f12',basis='ccpvdzf12',software='molpro'))": {
        'atom_corr': {
            'C': -0.5464261912627,
            'Cl': -0.3331232529849068,
            'F': 0.09684535337591452,
            'H': 0.3093277751661718,
            'N': 0.4773300729311916,
            'O': 0.6949720732175282,
            'S': -0.9142689727759676
        },
        'bond_corr_length': {
            'C': 64.67678783352589,
            'Cl': 6.316147607205602,
            'F': 2.9969902462203326e-14,
            'H': 1.8496519952345347e-16,
            'N': 9.624991083595463,
            'O': 1.0824291132601096e-15,
            'S': 735.661291892654
        },
        'bond_corr_neighbor': {
            'C': -0.024587039354705877,
            'Cl': -0.03540309101545116,
            'F': -0.016933453385969043,
            'H': 0.046660614206200754,
            'N': -0.0053021340471547,
            'O': -0.01078514461511072,
            'S': -0.13988268641251655
        },
        'mol_corr': 0.30287826305208276
    },

    "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": {
        'atom_corr': {
            'Br': -4.262780823587865,
            'C': 4.999999999999999,
            'Cl': -4.999999999999999,
            'F': -4.999999999999999,
            'H': -1.0450492093486716,
            'N': -4.999999999999999,
            'O': -4.999999999999999,
            'S': -4.999999999999999
        },
        'bond_corr_length': {
            'Br': 8692.219738590926,
            'C': 133.3489203999116,
            'Cl': 983.472669453573,
            'F': 98.4144446431002,
            'H': 0.9620481174299411,
            'N': 1.258833913444385e-27,
            'O': 356.54294878127047,
            'S': 4253.837243907855
        },
        'bond_corr_neighbor': {
            'Br': -0.637372927288811,
            'C': 0.07497384490455655,
            'Cl': 0.412600941322612,
            'F': 0.44818650615117767,
            'H': -0.9999999999999999,
            'N': -0.2675044921389425,
            'O': -0.16343725217730817,
            'S': 0.11474046296004109
        },
        'mol_corr': -3.096451394144581
    },

    "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": {
        'atom_corr': {
            'Br': -4.236702026546933,
            'C': 0.2049164817767285,
            'Cl': -2.5370579912419085,
            'F': -4.390697891358869,
            'H': -2.062847444255194,
            'N': -4.999999999999999,
            'O': -2.485820286098204,
            'S': -2.3806435571125646
        },
        'bond_corr_length': {
            'Br': 2886.4449179333255,
            'C': 0.05644392159534064,
            'Cl': 257.3272543651555,
            'F': 136.75193570503143,
            'H': 1.0783080754563377,
            'N': 4.0393833100316303e-35,
            'O': 120.00409931223447,
            'S': 301.39625436311553
        },
        'bond_corr_neighbor': {
            'Br': 0.27904803369228603,
            'C': -0.09439333163743208,
            'Cl': 0.17830274429860773,
            'F': 0.14749707198083395,
            'H': -0.1790691880962216,
            'N': -0.3694958066667204,
            'O': -0.07383806558254727,
            'S': -0.13458257713999408
        },
        'mol_corr': -3.782190737782739
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
             "LevelOfTheory(method='b97d3',basis='def2msvp',software='qchem')": 1.014,  # [4]
             "LevelOfTheory(method='wb97xd',basis='augccpvtz',software='gaussian')": 0.988,  # [3], taken as 'ωB97X-D/maug-cc-pVTZ'
             "LevelOfTheory(method='wb97xd',basis='6311++g(d,p)',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2tzvp',software='gaussian')": 0.988,  # [4]
             "LevelOfTheory(method='wb97xd',basis='def2svp',software='gaussian')": 0.986,  # [4]
             "LevelOfTheory(method='wb97xd3',basis='def2tzvp',software='qchem')": 0.984,  # [4]
             "LevelOfTheory(method='wb97mv',basis='def2tzvpd')": 1.002,  # [4]
             "LevelOfTheory(method='b2plypd3',basis='aug-cc-pvtz')": 0.995,  # [4]
             "LevelOfTheory(method='b2plypd3',basis='cc-pvtz')": 0.993,  # [4]
             "LevelOfTheory(method='b2plypd3',basis='def2tzvp')": 0.995,  # [4]
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
