# Psoccur_in_HexLayers.py
# MIT LICENSE 2016


#Get the number of parameter nodes in each hexcode layer with the occurrence
# of each FP layer.


#Get the list of ParameterIndices with each point layer.
import PointLayers
Pl_pitogether = PointLayers.Pl_pitogether


#Get the list of ParameterIndices of each hexcode layer.
import Zeb1HexcodeLayer
hexlayers = Zeb1HexcodeLayer.zeb1_layers ###****** choose this according
#  to the database file being used ******###


#Get the number of ParameterIndices with each point layer in each
# hexcode layer.
Pl_in_hexl = []

for i in range(0,len(Pl_pitogether)):
    for j in range(0,len(hexlayers)):
        Pl_in_hexl.append(len(set(Pl_pitogether[i]) & set(
            hexlayers[j])))
    print(Pl_in_hexl[(i)*len(hexlayers):((i+1)*len(hexlayers))])


