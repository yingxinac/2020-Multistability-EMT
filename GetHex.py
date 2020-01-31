# GetHex.py
# MIT LICENSE 2016


#Get the list of hexcodes corresponding to a given ParameterIndex in a
# parametergraph.

def get_hex(parameterindex,parametergraph):
    return [q.hex() for q in parametergraph.parameter(parameterindex).logic()]