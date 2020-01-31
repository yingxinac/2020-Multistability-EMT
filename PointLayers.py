# PointLayers.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each point layer (classify according to
# Zeb1, Snail1 and Ovol2).

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Zeb1notE.db") ###****** Choose
# database file
# properly******###

#Get the list of MorseGraphIndices with FP(i,j,*,*,*,k).
bounds000 = {"Zeb1":0,"Snail1":0,"Ovol2":0}
matches000 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database,
                                                   bounds000).matches()
bounds001 = {"Zeb1":0,"Snail1":0,"Ovol2":1}
matches001 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds001).matches()
bounds002 = {"Zeb1":0,"Snail1":0,"Ovol2":2}
matches002 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds002).matches()

bounds010 = {"Zeb1":0,"Snail1":1,"Ovol2":0}
matches010 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds010).matches()
bounds011 = {"Zeb1":0,"Snail1":1,"Ovol2":1}
matches011 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds011).matches()
bounds012 = {"Zeb1":0,"Snail1":1,"Ovol2":2}
matches012 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds012).matches()

bounds020 = {"Zeb1":0,"Snail1":2,"Ovol2":0}
matches020 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds020).matches()
bounds021 = {"Zeb1":0,"Snail1":2,"Ovol2":1}
matches021 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds021).matches()
bounds022 = {"Zeb1":0,"Snail1":2,"Ovol2":2}
matches022 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds022).matches()

bounds030 = {"Zeb1":0,"Snail1":3,"Ovol2":0}
matches030 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds030).matches()
bounds031 = {"Zeb1":0,"Snail1":3,"Ovol2":1}
matches031 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds031).matches()
bounds032 = {"Zeb1":0,"Snail1":3,"Ovol2":2}
matches032 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds032).matches()


bounds100 = {"Zeb1":1,"Snail1":0,"Ovol2":0}
matches100 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds100).matches()
bounds101 = {"Zeb1":1,"Snail1":0,"Ovol2":1}
matches101 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds101).matches()
bounds102 = {"Zeb1":1,"Snail1":0,"Ovol2":2}
matches102 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds102).matches()

bounds110 = {"Zeb1":1,"Snail1":1,"Ovol2":0}
matches110 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds110).matches()
bounds111 = {"Zeb1":1,"Snail1":1,"Ovol2":1}
matches111 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds111).matches()
bounds112 = {"Zeb1":1,"Snail1":1,"Ovol2":2}
matches112 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds112).matches()

bounds120 = {"Zeb1":1,"Snail1":2,"Ovol2":0}
matches120 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds120).matches()
bounds121 = {"Zeb1":1,"Snail1":2,"Ovol2":1}
matches121 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds121).matches()
bounds122 = {"Zeb1":1,"Snail1":2,"Ovol2":2}
matches122 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds122).matches()

bounds130 = {"Zeb1":1,"Snail1":3,"Ovol2":0}
matches130 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds130).matches()
bounds131 = {"Zeb1":1,"Snail1":3,"Ovol2":1}
matches131 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds131).matches()
bounds132 = {"Zeb1":1,"Snail1":3,"Ovol2":2}
matches132 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds132).matches()


bounds200 = {"Zeb1":2,"Snail1":0,"Ovol2":0}
matches200 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds200).matches()
bounds201 = {"Zeb1":2,"Snail1":0,"Ovol2":1}
matches201 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds201).matches()
bounds202 = {"Zeb1":2,"Snail1":0,"Ovol2":2}
matches202 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds202).matches()

bounds210 = {"Zeb1":2,"Snail1":1,"Ovol2":0}
matches210 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds210).matches()
bounds211 = {"Zeb1":2,"Snail1":1,"Ovol2":1}
matches211 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds211).matches()
bounds212 = {"Zeb1":2,"Snail1":1,"Ovol2":2}
matches212 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds212).matches()

bounds220 = {"Zeb1":2,"Snail1":2,"Ovol2":0}
matches220 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds220).matches()
bounds221 = {"Zeb1":2,"Snail1":2,"Ovol2":1}
matches221 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds221).matches()
bounds222 = {"Zeb1":2,"Snail1":2,"Ovol2":2}
matches222 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds222).matches()

bounds230 = {"Zeb1":2,"Snail1":3,"Ovol2":0}
matches230 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds230).matches()
bounds231 = {"Zeb1":2,"Snail1":3,"Ovol2":1}
matches231 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds231).matches()
bounds232 = {"Zeb1":2,"Snail1":3,"Ovol2":2}
matches232 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds232).matches()


bounds300 = {"Zeb1":3,"Snail1":0,"Ovol2":0}
matches300 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds300).matches()
bounds301 = {"Zeb1":3,"Snail1":0,"Ovol2":1}
matches301 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds301).matches()
bounds302 = {"Zeb1":3,"Snail1":0,"Ovol2":2}
matches302 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds302).matches()

bounds310 = {"Zeb1":3,"Snail1":1,"Ovol2":0}
matches310 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds310).matches()
bounds311 = {"Zeb1":3,"Snail1":1,"Ovol2":1}
matches311 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds311).matches()
bounds312 = {"Zeb1":3,"Snail1":1,"Ovol2":2}
matches312 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds312).matches()

bounds320 = {"Zeb1":3,"Snail1":2,"Ovol2":0}
matches320 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds320).matches()
bounds321 = {"Zeb1":3,"Snail1":2,"Ovol2":1}
matches321 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds321).matches()
bounds322 = {"Zeb1":3,"Snail1":2,"Ovol2":2}
matches322 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds322).matches()

bounds330 = {"Zeb1":3,"Snail1":3,"Ovol2":0}
matches330 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds330).matches()
bounds331 = {"Zeb1":3,"Snail1":3,"Ovol2":1}
matches331 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds331).matches()
bounds332 = {"Zeb1":3,"Snail1":3,"Ovol2":2}
matches332 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(database, bounds332).matches()


#Collect in layers.
matches_Pl1 = matches002
pilist_Pl1 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl1,
                                                         getparameterindex_object,database)
Pl1_pis = Pitogether.pitogether(pilist_Pl1)

matches_Pl2 = set(list(matches012)+list(matches102)+list(matches001))
pilist_Pl2 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl2,
                                                         getparameterindex_object,database)
Pl2_pis = Pitogether.pitogether(pilist_Pl2)

matches_Pl3 = set(list(matches202) + list(matches112) + list(matches022) +
                  list(matches101) + list(matches011) + list(matches000))
pilist_Pl3 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl3,
                                                         getparameterindex_object,database)
Pl3_pis = Pitogether.pitogether(pilist_Pl3)

matches_Pl4 = set(list(matches302) + list(matches212) + list(matches122) +
                  list(matches032) + list(matches201) + list(matches111) +
                  list(matches021) + list(matches100) + list(matches010))
pilist_Pl4 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl4,
                                                         getparameterindex_object,database)
Pl4_pis = Pitogether.pitogether(pilist_Pl4)

matches_Pl5 = set(list(matches301) + list(matches200) + list(matches312) +
                  list(matches211) + list(matches110) + list(matches222) +
                  list(matches121) + list(matches020) + list(matches132) +
                  list(matches031))
pilist_Pl5 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl5,
                                                         getparameterindex_object,database)
Pl5_pis = Pitogether.pitogether(pilist_Pl5)

matches_Pl6 = set(list(matches300) + list(matches311) + list(matches210) +
                  list(matches322) + list(matches221) + list(matches120) +
                  list(matches232) + list(matches131) + list(matches030))
pilist_Pl6 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl6,
                                                         getparameterindex_object,database)
Pl6_pis = Pitogether.pitogether(pilist_Pl6)

matches_Pl7 = set(list(matches310) + list(matches321) + list(matches220) +
                  list(matches332) + list(matches231) + list(matches130))
pilist_Pl7 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl7,
                                                         getparameterindex_object,database)
Pl7_pis = Pitogether.pitogether(pilist_Pl7)

matches_Pl8 = set(list(matches320) + list(matches230) + list(matches331))
pilist_Pl8 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl8,
                                                         getparameterindex_object,database)
Pl8_pis = Pitogether.pitogether(pilist_Pl8)

matches_Pl9 = matches330
pilist_Pl9 = MorseList_to_ParaList.MorseList_to_ParaList(matches_Pl9,
                                                         getparameterindex_object,database)
Pl9_pis = Pitogether.pitogether(pilist_Pl9)


Pl_pitogether = [Pl1_pis,Pl2_pis,Pl3_pis,
                 Pl4_pis,Pl5_pis,Pl6_pis,
                 Pl7_pis,Pl8_pis,Pl9_pis]

