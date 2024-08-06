from NetworkFunctions import functions
from Interfaces import Interface_Protocol
all_network_functions=[]
all_Interface=[]
all_Protocol=[]
def Interfaces_Protocols():
    for key in Interface_Protocol:
        all_Interface.append(key)
        all_Protocol.append(Interface_Protocol[key])
    return all_Interface, all_Protocol
def NetworkFunction():
    for i in functions:
        all_network_functions.append(i['Abbreviation'])

    return all_network_functions


