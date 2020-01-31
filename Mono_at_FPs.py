# Mono_at_FPs.py
# MIT LICENSE 2016


#Get the number of parameter nodes at which the system is monostable at each FP.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Ovol2notE.db") ### For different
# databases,
# just need to replace the database file here.

#Get the list of ParameterIndices with monostable.
monostable_query_object = DSGRN.Query.MonostableQuery.MonostableQuery(database)
monostable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    monostable_query_object.matches(),getparameterindex_object,database)
monostable_pitogether = Pitogether.pitogether(monostable_pilists)

#Get the list of ParameterIndices with each FP(i,j,*,*,*,k).
FP_pitogether=[]
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,3):
            bounds = {"Zeb1":i,"Snail1":j,"Ovol2":k}
            matches = DSGRN.Query.SingleFixedPointQuery\
                .SingleFixedPointQuery(database,
                                                      bounds).matches()
            FPpilists = MorseList_to_ParaList.MorseList_to_ParaList(matches,
                                                                 getparameterindex_object,database)
            FP_pitogether.append(Pitogether.pitogether(FPpilists))


mono_at_FP = []
for i in range(0,len(FP_pitogether)):
    mono_at_FP.append(len(set(monostable_pitogether) & set(FP_pitogether[i])))

print(mono_at_FP)
