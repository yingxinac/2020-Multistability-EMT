# PlayersMono_in_HexLayers.py
# MIT LICENSE 2016


#Get the number of parameter nodes in each hexcode layer at which the network
#  is monostable at each FP layer.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db") ###****** Choose
# database file
# properly ******###

#Get the list of ParameterIndices with monostable.
monostable_query_object = DSGRN.Query.MonostableQuery.MonostableQuery(database)
monostable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    monostable_query_object.matches(),getparameterindex_object,database)
monostable_pitogether = Pitogether.pitogether(monostable_pilists)

#Get the list of ParameterIndices with each point layer.
import PointLayers
Pl_pitogether = PointLayers.Pl_pitogether


#Get the list of ParameterIndices of each hexcode layer.
import Zeb1HexcodeLayer
hexlayers = Zeb1HexcodeLayer.zeb1_layers ###****** Choose this according
#  to the databese file being used ******###


#Get the number of ParameterIndices with each point layer in each
# hexcode layer.
Plmono_in_hexl = []

with open("players.txt","a") as f:
    for i in range(0,len(Pl_pitogether)):
        for j in range(0,len(hexlayers)):
            Plmono_in_hexl.append(len(set(Pl_pitogether[i]) & set(
                hexlayers[j]) & set(monostable_pitogether)))
        print(Plmono_in_hexl[(i)*len(hexlayers):((i+1)*len(hexlayers))])
        f.write("{}\n".format(Plmono_in_hexl[(i)*len(hexlayers):((i+1)*len(hexlayers))]))


