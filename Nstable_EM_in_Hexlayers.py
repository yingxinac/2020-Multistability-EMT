# Nstable_EM_in_Hexlayers.py
# MIT LICENSE 2016


#Get the number of parameter nodes in each hexcode layer for each nstable
# cases with E but without M, or with M but without E, or with both E and M,
# or with neither E nor M.

import DSGRN
import Data_added_GetParameterIndex as DGetParaIndex
import MorseList_to_ParaList
import Pitogether
getparameterindex_object = DGetParaIndex.Database.GetParameterIndex
database = DSGRN.Query.Database.Database("EMT_Ovol2notE.db") ###****** Change
# this database
# file
# as needed ******###

bounds002 = {"Zeb1":0,"Snail1":0,"Ovol2":2}
matches002 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(
    database, bounds002).matches()
pilists_002 = MorseList_to_ParaList.MorseList_to_ParaList(matches002,
                                                         getparameterindex_object, database)
P002_pitogether = Pitogether.pitogether(pilists_002)

bounds330 = {"Zeb1":3,"Snail1":3,"Ovol2":0}
matches330 = DSGRN.Query.SingleFixedPointQuery.SingleFixedPointQuery(
    database, bounds330).matches()
pilists_330 = MorseList_to_ParaList.MorseList_to_ParaList(matches330,
                                                         getparameterindex_object, database)
P330_pitogether = Pitogether.pitogether(pilists_330)

import Nstable_in_Hexlayers
print('The number of parameter nodes in each hexcode layer for each nstable '
      'cases:')
nstable_pitogether = Nstable_in_Hexlayers.nstable_pitogether
hexlayers = Nstable_in_Hexlayers.hexlayers

#In each nstable and each hexcode layer, number of parameter nodes with E
# state (FP(0,0,*,*,*,2)) but without M state (FP(3,3,*,*,*,0)).
nstable_in_hexlayers_002no330 = []
print('In each nstable and each hexcode layer, number of parameter nodes with E state (FP(0,0,*,*,*,2)) but without M state (FP(3,3,*,*,*,0)):')
for i in range(0,len(nstable_pitogether)):
    for j in range(0,len(hexlayers)):
        nstable_in_hexlayers_002no330.append(len(set(hexlayers[j]) & set(
            nstable_pitogether[i]) & set(P002_pitogether) - set(P330_pitogether)))
    print(nstable_in_hexlayers_002no330[(i * len(hexlayers)):((i + 1) * len(
        hexlayers))])
    print('**********')


#In each nstable and each hexcode layer, number of parameter nodes with M
# state (FP(3,3,*,*,*,0)) but without E state (FP(0,0,*,*,*,2)).
nstable_in_hexlayers_330no002 = []
print('In each nstable and each hexcode layer, number of parameter nodes with M state (FP(3,3,*,*,*,0)) but without E state (FP(0,0,*,*,*,2)):')
for i in range(0,len(nstable_pitogether)):
    for j in range(0,len(hexlayers)):
        nstable_in_hexlayers_330no002.append(len(set(hexlayers[j]) & set(
            nstable_pitogether[i]) & set(P330_pitogether) - set(P002_pitogether)))
    print(nstable_in_hexlayers_330no002[(i * len(hexlayers)):((i + 1) * len(
        hexlayers))])
    print('**********')

#In each nstable and each hexcode layer, number of parameter nodes with both M
# state (FP(3,3,*,*,*,0)) and E state (FP(0,0,*,*,*,2)).
nstable_in_hexlayers_330002 = []
print('In each nstable and each hexcode layer, number of parameter nodes with both M state (FP(3,3,*,*,*,0)) and E state (FP(0,0,*,*,*,2)):')
for i in range(0,len(nstable_pitogether)):
    for j in range(0,len(hexlayers)):
        nstable_in_hexlayers_330002.append(len(set(hexlayers[j]) & set(
            nstable_pitogether[i]) & set(P330_pitogether) & set(
            P002_pitogether)))
    print(nstable_in_hexlayers_330002[(i * len(hexlayers)):((i + 1) * len(
        hexlayers))])
    print('**********')

#In each nstable and each hexcode layer, number of parameter nodes with
# neither M state (FP(3,3,*,*,*,0)) nor E state (FP(0,0,*,*,*,2)).
nstable_in_hexlayers_no330002 = []
print('In each nstable and each hexcode layer, number of parameter nodes with neither M state (FP(3,3,*,*,*,0)) nor E state (FP(0,0,*,*,*,2)):')
for i in range(0,len(nstable_pitogether)):
    for j in range(0,len(hexlayers)):
        nstable_in_hexlayers_no330002.append(len(set(hexlayers[j]) & set(
            nstable_pitogether[i]) - set(P330_pitogether) - set(
            P002_pitogether)))
    print(nstable_in_hexlayers_no330002[(i * len(hexlayers)):((i + 1) * len(
        hexlayers))])
    print('**********')