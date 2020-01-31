# Ovol2HexcodeLayers.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each Ovol2 hexcode layer.

import DSGRN
import GetHex
import Ovol2hexcodei_pitogether
database = DSGRN.Query.Database.Database("EMT_Ovol2notE.db")
parameter_graph = database.parametergraph

#Get the list of Ovol2 hexcodes for all ParameterIndices.
all_hexonly_ovol2 = []
for k in range(0, parameter_graph.size()):
    all_hexonly_ovol2.append('*')

for i in range(0, parameter_graph.size()):
    all_hexonly_ovol2[i] = GetHex.get_hex(i, parameter_graph)[5]

#Get the list of ParamerIndices with Ovol2 hexcode being 'i':
ovol20_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('0',
                                                               all_hexonly_ovol2)

ovol24_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('4',
                                                               all_hexonly_ovol2)

ovol25_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('5',
                                                               all_hexonly_ovol2)

ovol2C_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('C',
                                                               all_hexonly_ovol2)

ovol2D_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('D',
                                                               all_hexonly_ovol2)

ovol2F_pitogether = Ovol2hexcodei_pitogether.ovol2i_pitogether('F',
                                                               all_hexonly_ovol2)

#Get the list of ParameterIndices of each Ovol2 hexcode layer.
ovol2_l1_pis = ovol20_pitogether
ovol2_l2_pis = ovol24_pitogether
ovol2_l3_pis = ovol25_pitogether + ovol2C_pitogether
ovol2_l4_pis = ovol2D_pitogether
ovol2_l5_pis = ovol2F_pitogether

ovol2_layers = [ovol2_l1_pis, ovol2_l2_pis, ovol2_l3_pis, ovol2_l4_pis,
                ovol2_l5_pis]


