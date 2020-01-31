# Ovol2hexcodei_pitogether.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each Ovol2 hexcode.

def ovol2i_pitogether(i,allhexonly):
    # From all ParameterIndices, pick the ones with Ovol2 hexcode = 'i'
    ovol2i_pi = []
    for j in range(0, len(allhexonly)):
        if allhexonly[j] == i:
            ovol2i_pi.append(j)

    return ovol2i_pi