# MorseList_to_ParaList.py
# MIT LICENSE 2016


def MorseList_to_ParaList(mgi_set, getparameterindex_object,database):
    # Get the list of ParameterIndex lists "pi_lists" corresponding to the set of
    # MorseGraphIndex mgi_set.  Each element is a list of PareameterIndices
    # corresponding to a MorseGraphIndex.

    pi_lists = []
    for k in range(0, len(mgi_set)):
        pi_lists.append('*')

    mgi_listpre = [list(x) for x in [mgi_set]]
    mgi_list = mgi_listpre[0]

    for i in range(0, len(mgi_set)):
        temp = getparameterindex_object(database,mgi_list[i])
        paraith = []
        for j in range(0, len(temp)):
            paraith.append(temp[j][0])

        pi_lists[i] = paraith

    #print(len(mgi_set))
    #print(len(pi_lists)) #These two should be the same

    # Count the total number of ParameterIndex in this list.
    #pi_lengthlist = []
    #for k in range(0, len(mgi_set)):
    #    pi_lengthlist.append('*')

    #for i in range(0, len(mgi_set)):
    #    pi_lengthlist[i] = len(pi_lists[i])

    #numberof_pi = sum(pi_lengthlist)
    #print(numberof_pi)

    return pi_lists