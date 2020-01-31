# Snail1hexcodeijk_pitogether.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each Snail1 hexcode.

def snail1ijk_pitogether(ijk,allhexonly):
    # From all ParameterIndices, pick the ones with Snail1 hexcode = 'ijk'
    snail1ijk_pi = []
    for i in range(0, len(allhexonly)):
        if allhexonly[i] == ijk:
            snail1ijk_pi.append(i)

    return snail1ijk_pi