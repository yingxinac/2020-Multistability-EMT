# Zeb1hexcodek_pitogether.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each Zeb1 hexcode.

def zeb1k_pitogether(k,allhexonly):
    # From all ParameterIndices, pick the ones with Zeb1 hexcode = 'k'
    zeb1k_pi = []
    for i in range(0, len(allhexonly)):
        if allhexonly[i] == k:
            zeb1k_pi.append(i)

    return zeb1k_pi