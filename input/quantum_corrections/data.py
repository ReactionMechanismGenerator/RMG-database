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
# All model chemistries here should be lower-case because the user input is changed to lower-case
atom_energies = {
    # Note: If your model chemistry does not include spin orbit coupling, you should add the corrections
    # to the energies here

    'wb97m-v/def2-tzvpd': {
        'H': -0.4941110259 + SOC['H'],
        'C': -37.8458797086 + SOC['C'],
        'N': -54.5915786724 + SOC['N'],
        'O': -75.0762279005 + SOC['O'],
        'S': -398.0789126541 + SOC['S'],
        'F': -99.7434924415 + SOC['F'],
        'Cl': -460.1100357269 + SOC['Cl'],
        'Br': -2573.9684615505 + SOC['Br']
    },

    # cbs-qb3 and cbs-qb3-paraskevas have the same corrections
    'cbs-qb3': {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },
    'cbs-qb3-paraskevas': {
        'H': -0.499818 + SOC['H'], 'N': -54.520543 + SOC['N'], 'O': -74.987624 + SOC['O'],
        'C': -37.785385 + SOC['C'], 'P': -340.817186 + SOC['P'], 'S': -397.657360 + SOC['S']
    },

    'm06-2x/cc-pvtz': {
        'H': -0.498135 + SOC['H'], 'N': -54.586780 + SOC['N'], 'O': -75.064242 + SOC['O'],
        'C': -37.842468 + SOC['C'], 'P': -341.246985 + SOC['P'], 'S': -398.101240 + SOC['S']
    },

    'g3': {
        'H': -0.5010030, 'N': -54.564343, 'O': -75.030991, 'C': -37.827717, 'P': -341.116432, 'S': -397.961110
    },

    # * indicates that the grid size used in the [QChem] electronic
    # structure calculation utilized 75 radial points and 434 angular points
    # (i.e,, this is specified in the $rem section of the [qchem] input file as: XC_GRID 000075000434)
    'm08so/mg3s*': {
        'H': -0.5017321350 + SOC['H'], 'N': -54.5574039365 + SOC['N'],
        'O': -75.0382931348 + SOC['O'], 'C': -37.8245648740 + SOC['C'],
        'P': -341.2444299005 + SOC['P'], 'S': -398.0940312227 + SOC['S']
    },

    'klip_1': {
        'H': -0.50003976 + SOC['H'], 'N': -54.53383153 + SOC['N'], 'O': -75.00935474 + SOC['O'],
        'C': -37.79266591 + SOC['C']
    },

    # Klip QCI(tz,qz)
    'klip_2': {
        'H': -0.50003976 + SOC['H'], 'N': -54.53169400 + SOC['N'], 'O': -75.00714902 + SOC['O'],
        'C': -37.79060419 + SOC['C']
    },

    # Klip QCI(dz,tz)
    'klip_3': {
        'H': -0.50005578 + SOC['H'], 'N': -54.53128140 + SOC['N'], 'O': -75.00356581 + SOC['O'],
        'C': -37.79025175 + SOC['C']
    },

    # Klip CCSD(T)(tz,qz)
    'klip_2_cc': {
        'H': -0.50003976 + SOC['H'], 'O': -75.00681155 + SOC['O'], 'C': -37.79029443 + SOC['C']
    },

    'ccsd(t)-f12/cc-pvdz-f12_h-tz': {
        'H': -0.499946213243 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    'ccsd(t)-f12/cc-pvdz-f12_h-qz': {
        'H': -0.499994558325 + SOC['H'], 'N': -54.526406291655 + SOC['N'],
        'O': -74.995458316117 + SOC['O'], 'C': -37.788203485235 + SOC['C']
    },

    # We are assuming that SOC is included in the Bond Energy Corrections
    'ccsd(t)-f12/cc-pvdz-f12': {
        'H': -0.499811124128, 'N': -54.526406291655, 'O': -74.995458316117,
        'C': -37.788203485235, 'S': -397.663040369707
    },

    'ccsd(t)-f12/cc-pvtz-f12': {
        'H': -0.499946213243, 'N': -54.53000909621, 'O': -75.004127673424,
        'C': -37.789862146471, 'S': -397.675447487865
    },

    'ccsd(t)-f12/cc-pvqz-f12': {
        'H': -0.499994558325, 'N': -54.530515226371, 'O': -75.005600062003,
        'C': -37.789961656228, 'S': -397.676719774973
    },

    'ccsd(t)-f12/cc-pcvdz-f12': {
        'H': -0.499811124128 + SOC['H'], 'N': -54.582137180344 + SOC['N'],
        'O': -75.053045547421 + SOC['O'], 'C': -37.840869118707 + SOC['C']
    },

    'ccsd(t)-f12/cc-pcvtz-f12': {
        'H': -0.499946213243 + SOC['H'], 'N': -54.588545831900 + SOC['N'],
        'O': -75.065995072347 + SOC['O'], 'C': -37.844662139972 + SOC['C']
    },

    'ccsd(t)-f12/cc-pcvqz-f12': {
        'H': -0.499994558325 + SOC['H'], 'N': -54.589137594139 + SOC['N'],
        'O': -75.067412234737 + SOC['O'], 'C': -37.844893820561 + SOC['C']
    },

    'ccsd(t)-f12/cc-pvtz-f12(-pp)': {
        'H': -0.499946213243 + SOC['H'], 'N': -54.53000909621 + SOC['N'],
        'O': -75.004127673424 + SOC['O'], 'C': -37.789862146471 + SOC['C'],
        'S': -397.675447487865 + SOC['S'], 'I': -294.81781766 + SOC['I']
    },

    # ccsd(t)/aug-cc-pvtz(-pp) atomic energies were fit to a set of 8 small molecules:
    # CH4, CH3OH, H2S, H2O, SO2, HI, I2, CH3I
    'ccsd(t)/aug-cc-pvtz(-pp)': {
        'H': -0.499821176024 + SOC['H'], 'O': -74.96738492 + SOC['O'],
        'C': -37.77385697 + SOC['C'], 'S': -397.6461604 + SOC['S'],
        'I': -294.7958443 + SOC['I']
    },

    # note that all atom corrections but S are fitted, the correction for S is calculated
    'ccsd(t)-f12/aug-cc-pvdz': {
        'H': -0.499459066131 + SOC['H'], 'N': -54.524279516472 + SOC['N'],
        'O': -74.992097308083 + SOC['O'], 'C': -37.786694171716 + SOC['C'],
        'S': -397.648733842400 + SOC['S']
    },

    'ccsd(t)-f12/aug-cc-pvtz': {
        'H': -0.499844820798 + SOC['H'], 'N': -54.527419359906 + SOC['N'],
        'O': -75.000001429806 + SOC['O'], 'C': -37.788504810868 + SOC['C'],
        'S': -397.666903000231 + SOC['S']
    },

    'ccsd(t)-f12/aug-cc-pvqz': {
        'H': -0.499949526073 + SOC['H'], 'N': -54.529569719016 + SOC['N'],
        'O': -75.004026586610 + SOC['O'], 'C': -37.789387892348 + SOC['C'],
        'S': -397.671214204994 + SOC['S']
    },

    'b-ccsd(t)-f12/cc-pvdz-f12': {
        'H': -0.499811124128 + SOC['H'], 'N': -54.523269942190 + SOC['N'],
        'O': -74.990725918500 + SOC['O'], 'C': -37.785409916465 + SOC['C'],
        'S': -397.658155086033 + SOC['S']
    },

    'b-ccsd(t)-f12/cc-pvtz-f12': {
        'H': -0.499946213243 + SOC['H'], 'N': -54.528135889213 + SOC['N'],
        'O': -75.001094055506 + SOC['O'], 'C': -37.788233578503 + SOC['C'],
        'S': -397.671745425929 + SOC['S']
    },

    'b-ccsd(t)-f12/cc-pvqz-f12': {
        'H': -0.499994558325 + SOC['H'], 'N': -54.529425753163 + SOC['N'],
        'O': -75.003820485005 + SOC['O'], 'C': -37.789006506290 + SOC['C'],
        'S': -397.674145126931 + SOC['S']
    },

    'b-ccsd(t)-f12/cc-pcvdz-f12': {
        'H': -0.499811124128 + SOC['H'], 'N': -54.578602780288 + SOC['N'],
        'O': -75.048064317367 + SOC['O'], 'C': -37.837592033417 + SOC['C']
    },

    'b-ccsd(t)-f12/cc-pcvtz-f12': {
        'H': -0.499946213243 + SOC['H'], 'N': -54.586402551258 + SOC['N'],
        'O': -75.062767632757 + SOC['O'], 'C': -37.842729156944 + SOC['C']
    },

    'b-ccsd(t)-f12/cc-pcvqz-f12': {
        'H': -0.49999456 + SOC['H'], 'N': -54.587781507581 + SOC['N'],
        'O': -75.065397706471 + SOC['O'], 'C': -37.843634971592 + SOC['C']
    },

    'b-ccsd(t)-f12/aug-cc-pvdz': {
        'H': -0.499459066131 + SOC['H'], 'N': -54.520475581942 + SOC['N'],
        'O': -74.986992215049 + SOC['O'], 'C': -37.783294495799 + SOC['C']
    },

    'b-ccsd(t)-f12/aug-cc-pvtz': {
        'H': -0.499844820798 + SOC['H'], 'N': -54.524927371700 + SOC['N'],
        'O': -74.996328829705 + SOC['O'], 'C': -37.786320700792 + SOC['C']
    },

    'b-ccsd(t)-f12/aug-cc-pvqz': {
        'H': -0.499949526073 + SOC['H'], 'N': -54.528189769291 + SOC['N'],
        'O': -75.001879610563 + SOC['O'], 'C': -37.788165047059 + SOC['C']
    },

    'mp2_rmp2_pvdz': {
        'H': -0.49927840 + SOC['H'], 'N': -54.46141996 + SOC['N'], 'O': -74.89408254 + SOC['O'],
        'C': -37.73792713 + SOC['C']
    },
    # Calculated atomic energies fitted orca 4.2.1  dlpno-ccsd(t)/def2-tzvp NormalPNO
    # geometries are optimized at wb97xd/def2ztvp (g16)
    # fitted using Colin's BAC algorithm and SOC are included in the correction
    # AEs are fitted to neutral  and cation molecules with RMSE and MAE 7.99 and 5.96 kJ/mol respectively.
    'dlpno-ccsd(t)/def2-tzvp': {
        'H': -0.49641082 + SOC['H'], 'C': -37.77260625 + SOC['C'], 'N': -54.50388932 + SOC['N'],
        'O': -74.96724914 + SOC['O'], 'F': -99.61983419 + SOC['F'], 'S': -397.63390936 + SOC['S'],
        'Cl': -459.6565116 + SOC['Cl']
    },

    'mp2_rmp2_pvtz': {
        'H': -0.49980981 + SOC['H'], 'N': -54.49615972 + SOC['N'], 'O': -74.95506980 + SOC['O'],
        'C': -37.75833104 + SOC['C']
    },

    'mp2_rmp2_pvqz': {
        'H': -0.49994557 + SOC['H'], 'N': -54.50715868 + SOC['N'], 'O': -74.97515364 + SOC['O'],
        'C': -37.76533215 + SOC['C']
    },

    'ccsd-f12/cc-pvdz-f12': {
        'H': -0.499811124128 + SOC['H'], 'N': -54.524325513811 + SOC['N'],
        'O': -74.992326577897 + SOC['O'], 'C': -37.786213495943 + SOC['C']
    },

    'ccsd(t)-f12/cc-pvdz-f12_noscale': {
        'H': -0.499811124128 + SOC['H'], 'N': -54.526026290887 + SOC['N'],
        'O': -74.994751897699 + SOC['O'], 'C': -37.787881871511 + SOC['C']
    },

    'g03_pbepbe_6-311++g_d_p': {
        'H': -0.499812273282 + SOC['H'], 'N': -54.5289567564 + SOC['N'],
        'O': -75.0033596764 + SOC['O'], 'C': -37.7937388736 + SOC['C']
    },

    'fci/cc-pvdz': {
        'C': -37.789527 + SOC['C']
    },

    'fci/cc-pvtz': {
        'C': -37.781266669684 + SOC['C']
    },

    'fci/cc-pvqz': {
        'C': -37.787052110598 + SOC['C']
    },

    # 'bmk/cbsb7' and 'bmk/6-311g(2d,d,p)' have the same corrections
    'bmk/cbsb7': {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },
    'bmk/6-311g(2d,d,p)': {
        'H': -0.498618853119 + SOC['H'], 'N': -54.5697851544 + SOC['N'],
        'O': -75.0515210278 + SOC['O'], 'C': -37.8287310027 + SOC['C'],
        'P': -341.167615941 + SOC['P'], 'S': -398.001619915 + SOC['S']
    },

    # Fitted to small molecules
    'b3lyp/6-31g(d,p)': {
        'H': -0.500426155, 'C': -37.850331697831, 'O': -75.0535872748806, 'S': -398.100820107242
    },

    # Calculated atomic energies
    'b3lyp/6-311+g(3df,2p)': {
        'H': -0.502155915123 + SOC['H'], 'C': -37.8574709934 + SOC['C'],
        'N': -54.6007233609 + SOC['N'], 'O': -75.0909131284 + SOC['O'],
        'P': -341.281730319 + SOC['P'], 'S': -398.134489850 + SOC['S']
    },

    'wb97x-d/aug-cc-pvtz': {
        'H': -0.502803 + SOC['H'], 'N': -54.585652 + SOC['N'], 'O': -75.068286 + SOC['O'],
        'C': -37.842014 + SOC['C']
    },
    # wb97xd/def2tzvp conducted using G16.
    # geometries are optimized at wb97xd/def2ztvp (g16)
    # fitted using Colin's BAC algorithm and SOC are included in the correction
    # AEs are fitted to neutral and cation molecules with RMSE and MAE 9.16 and 6.66 kJ/mol respectively.
    'wb97xd/def2tzvp': {
        'H': -0.50224721 + SOC['H'], 'C': -37.84221823 + SOC['C'], 'N': -54.58757237 + SOC['N'],
        'O': -75.06946654 + SOC['O'], 'F': -99.74118694 + SOC['F'], 'S': -398.10676342 + SOC['S'],
        'Cl': -460.14516264 + SOC['Cl']
    },
    # Calculated atomic energies (unfitted)
    'MRCI+Davidson/aug-cc-pV(T+d)Z': {
        'H': -0.49982118 + SOC['H'], 'C': -37.78321274 + SOC['C'], 'N': -54.51729444 + SOC['N'],
        'O': -74.97847534 + SOC['O'], 'S': -397.6571654 + SOC['S']
    },

}

# Petersson-type bond additivity correction parameters
pbac = {

    # 'S-H', 'C-S', 'C=S', 'S-S', 'O-S', 'O=S', 'O=S=O' taken from http://hdl.handle.net/1721.1/98155 (both for
    # 'CCSD(T)-F12/cc-pVDZ-F12' and 'CCSD(T)-F12/cc-pVTZ-F12')
    'ccsd(t)-f12/cc-pvdz-f12': {
        'C-H': -0.46, 'C-C': -0.68, 'C=C': -1.90, 'C#C': -3.13,
        'O-H': -0.51, 'C-O': -0.23, 'C=O': -0.69, 'O-O': -0.02, 'C-N': -0.67,
        'C=N': -1.46, 'C#N': -2.79, 'N-O': 0.74, 'N_O': -0.23, 'N=O': -0.51,
        'N-H': -0.69, 'N-N': -0.47, 'N=N': -1.54, 'N#N': -2.05, 'S-H': 0.87,
        'C-S': 0.42, 'C=S': 0.51, 'S-S': 0.86, 'O-S': 0.23, 'O=S': -0.53,
        'O=S=O': 1.95
    },

    'ccsd(t)-f12/cc-pvtz-f12': {
        'C-H': -0.09, 'C-C': -0.27, 'C=C': -1.03, 'C#C': -1.79,
        'O-H': -0.06, 'C-O': 0.14, 'C=O': -0.19, 'O-O': 0.16, 'C-N': -0.18,
        'C=N': -0.41, 'C#N': -1.41, 'N-O': 0.87, 'N_O': -0.09, 'N=O': -0.23,
        'N-H': -0.01, 'N-N': -0.21, 'N=N': -0.44, 'N#N': -0.76, 'S-H': 0.52,
        'C-S': 0.13, 'C=S': -0.12, 'S-S': 0.30, 'O-S': 0.15, 'O=S': -2.61,
        'O=S=O': 0.27
    },

    'ccsd(t)-f12/cc-pvqz-f12': {
        'C-H': -0.08, 'C-C': -0.26, 'C=C': -1.01, 'C#C': -1.66,
        'O-H': 0.07, 'C-O': 0.25, 'C=O': -0.03, 'O-O': 0.26, 'C-N': -0.20,
        'C=N': -0.30, 'C#N': -1.33, 'N-O': 1.01, 'N_O': -0.03, 'N=O': -0.26,
        'N-H': 0.06, 'N-N': -0.23, 'N=N': -0.37, 'N#N': -0.64
    },
    # fitted using Colin's BAC algorithm and AC are included in the correction units kcal/mol
    # BACs are fitted to neutral molecules with RMSE and MAE 5.50 and 3.58 kJ/mol respectively.
    'dlpno-ccsd(t)/def2-tzvp': {
        'Cl-F': -0.07683, 'N=N': 1.20853, 'N=O': 1.49303, 'Cl-H': 0.00108,
        'Cl-N': -0.31383, 'Cl-O': 0.13871, 'Cl-S': -1.26284, 'C-O': -0.04381, 'C-N': -0.42627,
        'C-Cl': -0.03151, 'Cl-Cl': -0.22919, 'C-H': 0.12906, 'C-F': 0.37444, 'C-C': -0.43463,
        'S=S': -0.39416, 'C#O': 2.70341, 'C#N': 1.37471, 'C-S': -0.03749, 'C#C': -0.66008,
        'O-O': 0.09663, 'C=S': 0.80888, 'H-S': 1.23648, 'C=O': 0.88066, 'C=N': 0.03998,
        'H-N': -0.49564, 'H-O': -0.41183, 'H-H': 0.6263, 'N#N': 3.71325, 'N-N': 0.74915,
        'N-O': -0.62156, 'C=C': -0.63901, 'O=S': -1.39626, 'O-S': -1.37002, 'S-S': 0.1515,
        'F-S': -0.68693, 'F-O': 0.09202, 'F-H': -1.68214, 'F-F': 0.95483, 'O=O': -2.64949
    },

    'cbs-qb3': {
        'C-H': -0.11, 'C-C': -0.30, 'C=C': -0.08, 'C#C': -0.64, 'O-H': 0.02, 'C-O': 0.33, 'C=O': 0.55,
        # Table IX: Petersson GA (1998) J. of Chemical Physics, DOI: 10.1063/1.477794
        'N-H': -0.42, 'C-N': -0.13, 'C#N': -0.89, 'C-F': 0.55, 'C-Cl': 1.29, 'S-H': 0.0, 'C-S': 0.43,
        'O=S': -0.78,
        'N=O': 1.11, 'N-N': -1.87, 'N=N': -1.58, 'N-O': 0.35,
        # Table 2: Ashcraft R (2007) J. Phys. Chem. B; DOI: 10.1021/jp073539t
        'N#N': -2.0, 'O=O': -0.2, 'H-H': 1.1,  # Unknown source
    },

    'cbs-qb3-paraskevas': {
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
    'b3lyp/cbsb7': {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    'b3lyp/6-311g(2d,d,p)': {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    'b3lyp/6-311+g(3df,2p)': {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    'b3lyp/6-31g(d,p)': {
        'C-H': 0.25, 'C-C': -1.89, 'C=C': -0.40, 'C#C': -1.50,
        'O-H': -1.09, 'C-O': -1.18, 'C=O': -0.01, 'N-H': 1.36, 'C-N': -0.44,
        'C#N': 0.22, 'C-S': -2.35, 'O=S': -5.19, 'S-H': -0.52,
    },
    # fitted using Colin's BAC algorithm and AC are included in the correction units kcal/mol
    # BACs are fitted to neutral molecules with RMSE and MAE 6.01 and 4.40 kJ/mol respectively.
    'wb97xd/def2tzvp': {
        'Cl-F': -0.28278, 'N=N': 0.33647, 'N=O': -0.03659, 'Cl-H': -0.7062,
        'Cl-N': 0.74929, 'Cl-O': -0.30864, 'Cl-S': 0.09203, 'C-O': 0.11458, 'C-N': 0.5263, 'C-Cl': 0.10176,
        'Cl-Cl': 0.76157, 'C-H': -0.05318, 'C-F': 0.54033, 'C-C': 0.19475, 'S=S': -2.68004, 'C#O': -2.32306,
        'C#N': -2.28647, 'C-S': -0.10163, 'C#C': -2.4399, 'O-O': 0.34803, 'C=S': -0.16988, 'H-S': 0.74414,
        'C=O': 1.00501, 'C=N': -0.68305, 'H-N': -0.52232, 'H-O': -1.18129, 'H-H': -1.76862, 'N#N': -3.84259,
        'N-N': 2.66325, 'N-O': 1.69619, 'C=C': -0.11192, 'O=S': -1.33397, 'O-S': -1.71863, 'S-S': 0.5224,
        'F-S': -1.28933, 'F-O': -0.03756, 'F-H': -3.71018, 'F-F': -1.71494, 'O=O': -6.70857
    },
}

# Melius-type bond additivity correction parameters
mbac = {
    # fitted using Colin's BAC algorithm and AC are included in the correction units kcal/mol
    # BACs are fitted to neutral molecules with RMSE and MAE 5.69 and 3.86 kJ/mol respectively.
    'dlpno-ccsd(t)/def2-tzvp': {
        'atom_corr': {
            'C': -2.54554, 'F': -0.40263, 'H': 0.26804, 'Cl': -0.54209, 'O': -0.57949, 'N': -2.20529, 'S': -1.84913},
        'bond_corr_length': {
            'C': -0.23276, 'F': -0.04107, 'H': 0.23988, 'Cl': 0.22409, 'O': 0.38914, 'N': 0.10006, 'S': 0.21389},
        'bond_corr_neighbor': {
            'C': 4.29082, 'F': 0.47779, 'H': 0.01691, 'Cl': 0.46756, 'O': 0.03281, 'N': 1.41962, 'S': 0.70839}},

    # fitted using Colin's BAC algorithm and AC are included in the correction units kcal/mol
    # BACs are fitted to neutral molecules with RMSE and MAE 7.36 and 5.44 kJ/mol respectively.
    'wb97xd/def2tzvp': {
        'atom_corr': {
            'C': 0.62251, 'F': -0.89735, 'H': -0.17636, 'Cl': -0.71731, 'O': -1.80025, 'N': 1.28276, 'S': -1.37114},
        'bond_corr_length': {
            'C': -0.04942, 'F': 0.13823, 'H': 0.08243, 'Cl': 0.25196, 'O': 0.25446, 'N': -0.19574, 'S': 0.16428},
        'bond_corr_neighbor': {
            'C': 0.0, 'F': 1.12461, 'H': 0.89579, 'Cl': 0.57391, 'O': 2.4297, 'N': 0.01577, 'S': 0.79889}}
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

freq_dict = {'hf/sto-3g': 0.817,  # [2]
             'hf/6-31g': 0.903,  # [2]
             'hf/6-31g(d)': 0.899,  # [2]
             'hf/6-31g(d,p)': 0.903,  # [2]
             'hf/6-31g+(d,p)': 0.904,  # [2]
             'hf/6-31+g(d,p)': 0.915 * 1.014,  # [1] Table 7
             'pm3': 0.940 * 1.014,  # [1] Table 7, the 0.940 value is the ZPE scale factor
             'pm6': 1.078 * 1.014,  # [1] Table 7, the 1.078 value is the ZPE scale factor
             'b3lyp/6-31g(d,p)': 0.961,  # [2]
             'b3lyp/6-311g(d,p)': 0.967,  # [2]
             'b3lyp/6-311+g(3df,2p)': 0.967,  # [2]
             'b3lyp/6-311+g(3df,2pd)': 0.970,  # [2]
             'm06-2x/6-31g(d,p)': 0.952,  # [2]
             'm06-2x/6-31+g(d,p)': 0.979,  # [3]
             'm06-2x/6-311+g(d,p)': 0.983,  # [3]
             'm06-2x/6-311++g(d,p)': 0.983,  # [3]
             'm06-2x/cc-pvtz': 0.955,  # [2]
             'm06-2x/aug-cc-pvdz': 0.993,  # [3]
             'm06-2x/aug-cc-pvtz': 0.985,  # [1] Table 3, [3]
             'm06-2x/def2-tzvp': 0.984,  # [3]
             'm06-2x/def2-qzvp': 0.983,  # [3]
             'm06-2x/def2-tzvpp': 0.983,  # [1] Table 3, [3]
             'm08so/mg3s*': 0.995,  # [1] Table 3, taken as 'M08-SO/MG3S'
             'wb97x-d/aug-cc-pvtz': 0.988,  # [3], taken as 'ωB97X-D/maug-cc-pVTZ'
             'wb97xd/6-311++g(d,p)': 0.988,  # [4]
             'wb97xd/def2tzvp': 0.988,  # [4]
             'wb97xd/def2svp': 0.986,  # [4]
             'apfd/def2tzvp': 0.993,  # [4]
             'apfd/def2tzvpp': 0.992,  # [4]
             'mp2_rmp2_pvdz': 0.953,  # [2], taken as 'MP2/cc-pVDZ'
             'mp2_rmp2_pvtz': 0.950,  # [2], taken as 'MP2/cc-pVTZ'
             'mp2_rmp2_pvqz': 0.962,  # [2], taken as 'MP2/cc-pVQZ'
             'cbs-qb3': 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             'cbs-qb3-paraskevas': 0.99 * 1.014,  # [5], the 0.99 value is the ZPE scale factor of CBS-QB3
             'ccsd-f12/cc-pvdz-f12': 0.947,  # [2], taken as 'CCSD/cc-pVDZ'
             'ccsd(t)/cc-pvdz': 0.979,  # [2]
             'ccsd(t)/cc-pvtz': 0.975,  # [2]
             'ccsd(t)/cc-pvqz': 0.970,  # [2]
             'ccsd(t)/aug-cc-pvdz': 0.963,  # [2]
             'ccsd(t)/aug-cc-pvtz': 1.001,  # [3]
             'ccsd(t)/aug-cc-pvqz': 0.975,  # [2]
             'ccsd(t)/cc-pv(t+d)z': 0.965,  # [2]
             'ccsd(t)-f12/cc-pvdz-f12': 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             'ccsd(t)-f12/cc-pvtz-f12': 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             'ccsd(t)-f12/cc-pvqz-f12': 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             'ccsd(t)-f12/cc-pcvdz-f12': 0.997,  # [3], taken as 'CCSD(T)-F12a/cc-pVDZ-F12'
             'ccsd(t)-f12/cc-pcvtz-f12': 0.998,  # [3], taken as 'CCSD(T)-F12a/cc-pVTZ-F12'
             'ccsd(t)-f12/aug-cc-pvdz': 0.997,  # [3], taken as 'CCSD(T)/cc-pVDZ'
             'ccsd(t)-f12/aug-cc-pvtz': 0.998,  # [3], taken as CCSD(T)-F12a/cc-pVTZ-F12
             'ccsd(t)-f12/aug-cc-pvqz': 0.998,  # [3], taken as 'CCSD(T)-F12b/VQZF12//CCSD(T)-F12a/TZF'
             }
