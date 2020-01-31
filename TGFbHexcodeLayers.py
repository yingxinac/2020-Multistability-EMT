# TGFbHexcodeLayers.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each TGFb hexcode layer.

import DSGRN
import GetHex
import TGFbhexcodei_pitogether
database = DSGRN.Query.Database.Database("EMT_TGFbnotE.db")
parameter_graph = database.parametergraph

#Get the list of TGFb hexcodes for all ParameterIndices.
all_hexonly_tgfb = []
for k in range(0, parameter_graph.size()):
    all_hexonly_tgfb.append('*')

for i in range(0, parameter_graph.size()):
    all_hexonly_tgfb[i] = GetHex.get_hex(i, parameter_graph)[4]

#Get the list of ParamerIndices with TGFb hexcode being 'i':
tgfb0_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('0',
                                                               all_hexonly_tgfb)

tgfb8_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('8',
                                                               all_hexonly_tgfb)

tgfbA_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('A',
                                                               all_hexonly_tgfb)

tgfbC_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('C',
                                                               all_hexonly_tgfb)

tgfbE_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('E',
                                                               all_hexonly_tgfb)

tgfbF_pitogether = TGFbhexcodei_pitogether.tgfbi_pitogether('F',
                                                               all_hexonly_tgfb)

#Get the list of ParameterIndices of each TGFb hexcode layer.
tgfb_l1_pis = tgfb0_pitogether
tgfb_l2_pis = tgfb8_pitogether
tgfb_l3_pis = tgfbA_pitogether + tgfbC_pitogether
tgfb_l4_pis = tgfbE_pitogether
tgfb_l5_pis = tgfbF_pitogether

tgfb_layers = [tgfb_l1_pis, tgfb_l2_pis, tgfb_l3_pis, tgfb_l4_pis,
               tgfb_l5_pis]