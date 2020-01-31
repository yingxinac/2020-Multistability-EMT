# Nstable_in_Hexlayers.py
# MIT LICENSE 2016


#Get the number of parameter nodes in each hexcode layer for each nstable cases.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db") ###****** Change
# this database file
# as needed ******###


#Get the list of ParameterIndices with monostable.
monostable_query_object = DSGRN.Query.MonostableQuery.MonostableQuery(database)
monostable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    monostable_query_object.matches(),getparameterindex_object,database)
monostable_pitogether = Pitogether.pitogether(monostable_pilists)


#Get the list of ParameterIndices with bistable.
bistable_query_object = DSGRN.Query.BistableQuery.BistableQuery(database)
bistable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    bistable_query_object.matches(),getparameterindex_object,database)
bistable_pitogether = Pitogether.pitogether(bistable_pilists)


nstable_query = DSGRN.Query.NstableQuery.NstableQuery

tristable_query_object = nstable_query(database, 3)
tri_matches_pre = tristable_query_object.matches()

fourstable_query_object = nstable_query(database, 4)
four_matches_pre = fourstable_query_object.matches()

fivestable_query_object = nstable_query(database, 5)
five_matches_pre = fivestable_query_object.matches()

sixstable_query_object = nstable_query(database, 6)
six_matches_pre = sixstable_query_object.matches()

sevenstable_query_object = nstable_query(database, 7)
seven_matches_pre = sevenstable_query_object.matches()

eightstable_query_object = nstable_query(database, 8)
eight_matches_pre = eightstable_query_object.matches()

#-------------------------------------------------------------------------------
tri_matches = tri_matches_pre - four_matches_pre
tri_pilists = MorseList_to_ParaList.MorseList_to_ParaList(tri_matches,
                                                          getparameterindex_object, database)
tri_pitogether = Pitogether.pitogether(tri_pilists)


four_matches = four_matches_pre - five_matches_pre
four_pilists = MorseList_to_ParaList.MorseList_to_ParaList(four_matches,
                                                          getparameterindex_object, database)
four_pitogether = Pitogether.pitogether(four_pilists)


five_matches = five_matches_pre - six_matches_pre
five_pilists = MorseList_to_ParaList.MorseList_to_ParaList(five_matches,
                                                          getparameterindex_object, database)
five_pitogether = Pitogether.pitogether(five_pilists)


six_matches = six_matches_pre - seven_matches_pre
six_pilists = MorseList_to_ParaList.MorseList_to_ParaList(six_matches,
                                                          getparameterindex_object, database)
six_pitogether = Pitogether.pitogether(six_pilists)


seven_matches = seven_matches_pre - eight_matches_pre
seven_pilists = MorseList_to_ParaList.MorseList_to_ParaList(seven_matches,
                                                          getparameterindex_object, database)
seven_pitogether = Pitogether.pitogether(seven_pilists)


eight_matches = eight_matches_pre
eight_pilists = MorseList_to_ParaList.MorseList_to_ParaList(eight_matches,
                                                            getparameterindex_object, database)
eight_pitogether = Pitogether.pitogether(eight_pilists)

nstable_pitogether = [monostable_pitogether, bistable_pitogether,
                      tri_pitogether, four_pitogether, five_pitogether,
                      six_pitogether, seven_pitogether, eight_pitogether]

import Zeb1HexcodeLayer
hexlayers = Zeb1HexcodeLayer.zeb1_layers ###****** Define hexlayers
# according to the database file being used ******###

nstable_in_hexlayers = []

for i in range(0,len(nstable_pitogether)):
    for j in range(0,len(hexlayers)):
        nstable_in_hexlayers.append(len(set(hexlayers[j]) & set(
            nstable_pitogether[i])))
    print(nstable_in_hexlayers[(i * len(hexlayers)):((i + 1) * len(hexlayers))])
    print('**********')



