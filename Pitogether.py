# Pitogether.py
# MIT LICENSE 2016


def pitogether(pilists):
    # Put the ParameterIndices in a list of lists of ParameterIndices together
    # as a single list.

    pi_together = []
    for i in range(0, len(pilists)):
        for j in range(0, len(pilists[i])):
            pi_together.append(pilists[i][j])


    return pi_together