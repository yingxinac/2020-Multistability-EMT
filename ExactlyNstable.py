# ExactlyNstable.py
# MIT LICENSE 2016

# Get the number of parameter nodes at which there are exactly n FPs,
# for n =1,2,3,4,5,6,7,8.  Also show the number of parameter nodes at which
# there are multiple FPs.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db") ###****** Chose
# the database file
# properly ******###
parameter_graph = database.parametergraph

#Total number of parameter nodes:
print('The total number of parameter nodes is:')
print(parameter_graph.size())

#Get the list of ParameterIndices with monostable.
monostable_query_object = DSGRN.Query.MonostableQuery.MonostableQuery(database)
monostable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    monostable_query_object.matches(),getparameterindex_object,database)
print('Number of monostable MorseGraphIndices:')
print(len(monostable_pilists))
monostable_pitogether = Pitogether.pitogether(monostable_pilists)
print('Number of monostable ParameterIndices:')
print(len(monostable_pitogether))


#Get the list of ParameterIndices with bistable.
bistable_query_object = DSGRN.Query.BistableQuery.BistableQuery(database)
bistable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    bistable_query_object.matches(),getparameterindex_object,database)
print('Number of bistable MorseGraphIndices:')
print(len(bistable_pilists))
bistable_pitogether = Pitogether.pitogether(bistable_pilists)
print('Number of bistable ParameterIndices:')
print(len(bistable_pitogether))


#Get the list of ParameterIndices with multistable.
multistable_query_object = DSGRN.Query.MultistableQuery.MultistableQuery(
    database)
multistable_pilists = MorseList_to_ParaList.MorseList_to_ParaList(
    multistable_query_object.matches(),getparameterindex_object,database)
print('Number of multistable MorseGraphIndices:')
print(len(multistable_pilists))
multistable_pitogether = Pitogether.pitogether(multistable_pilists)
print('Number of multistable ParameterIndices:')
print(len(multistable_pitogether))

nstable_query = DSGRN.Query.NstableQuery.NstableQuery

tristable_query_object = nstable_query(database, 3)
tri_matches_pre = tristable_query_object.matches()
print("Number of MorseGraphIndices with at least 3 FPs:")
print(len(tri_matches_pre))

fourstable_query_object = nstable_query(database, 4)
four_matches_pre = fourstable_query_object.matches()
print("Number of MorseGraphIndices with at least 4 FPs:")
print(len(four_matches_pre))

fivestable_query_object = nstable_query(database, 5)
five_matches_pre = fivestable_query_object.matches()
print("Number of MorseGraphIndices with at least 5 FPs:")
print(len(five_matches_pre))

sixstable_query_object = nstable_query(database, 6)
six_matches_pre = sixstable_query_object.matches()
print("Number of MorseGraphIndices with at least 6 FPs:")
print(len(six_matches_pre))

sevenstable_query_object = nstable_query(database, 7)
seven_matches_pre = sevenstable_query_object.matches()
print("Number of MorseGraphIndices with at least 7 FPs:")
print(len(seven_matches_pre))

eightstable_query_object = nstable_query(database, 8)
eight_matches_pre = eightstable_query_object.matches()
print("Number of MorseGraphIndices with at least 8 FPs:")
print(len(eight_matches_pre))

#-------------------------------------------------------------------------------
tri_matches = tri_matches_pre - four_matches_pre
print('Number of MorseGraphIndices with exactly 3 FPs:')
print(len(tri_matches))
tri_pilists = MorseList_to_ParaList.MorseList_to_ParaList(tri_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
tri_pitogether = Pitogether.pitogether(tri_pilists)
print('Number of ParameterIndices with exactly 3 FPs:')
print(len(tri_pitogether))


four_matches = four_matches_pre - five_matches_pre
print('Number of MorseGraphIndices with exactly 4 FPs:')
print(len(four_matches))
four_pilists = MorseList_to_ParaList.MorseList_to_ParaList(four_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
four_pitogether = Pitogether.pitogether(four_pilists)
print('Number of ParameterIndices with exactly 4 FPs:')
print(len(four_pitogether))


five_matches = five_matches_pre - six_matches_pre
print('Number of MorseGraphIndices with exactly 5 FPs:')
print(len(five_matches))
five_pilists = MorseList_to_ParaList.MorseList_to_ParaList(five_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
five_pitogether = Pitogether.pitogether(five_pilists)
print('Number of ParameterIndices with exactly 5 FPs:')
print(len(five_pitogether))


six_matches = six_matches_pre - seven_matches_pre
print('Number of MorseGraphIndices with exactly 6 FPs:')
print(len(six_matches))
six_pilists = MorseList_to_ParaList.MorseList_to_ParaList(six_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
six_pitogether = Pitogether.pitogether(six_pilists)
print('Number of ParameterIndices with exactly 6 FPs:')
print(len(six_pitogether))


seven_matches = seven_matches_pre - eight_matches_pre
print('Number of MorseGraphIndices with exactly 7 FPs:')
print(len(seven_matches))
seven_pilists = MorseList_to_ParaList.MorseList_to_ParaList(seven_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
seven_pitogether = Pitogether.pitogether(seven_pilists)
print('Number of ParameterIndices with exactly 7 FPs:')
print(len(seven_pitogether))

eight_matches = eight_matches_pre
print('Number of MorseGraphIndices with exactly 8 FPs:')
print(len(eight_matches))
eight_pilists = MorseList_to_ParaList.MorseList_to_ParaList(eight_matches,
                                                          getparameterindex_object, database)
#Put the ParameterIndices together
eight_pitogether = Pitogether.pitogether(eight_pilists)
print('Number of ParameterIndices with exactly 8 FPs:')
print(len(eight_pitogether))