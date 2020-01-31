# TGFbhexcodei_pitogether.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each TGFb hexcode.

def tgfbi_pitogether(j,allhexonly):
    # From all ParameterIndices, pick the ones with TGFb hexcode = 'j'
    tgfbi_pi = []
    for i in range(0, len(allhexonly)):
        if allhexonly[i] == j:
            tgfbi_pi.append(i)

    return tgfbi_pi