import DSGRN
import GetHex
import json

def make_layer_dict(db="EMT_Zeb1notE.db"):
    # The following should be an input argument from sys
    database = DSGRN.Query.Database.Database(db)

    # Get hex codes for layers
    zquery = DSGRN.SingleGeneQuery(database, "Zeb1")
    graph = zquery(0)
    layersdict = graph.data
    hexes = [val[0] for _,val in layersdict.items()]

    #Get the list of parameters for each Zeb1 hexcode
    parameter_graph = database.parametergraph
    zeb1_pitogether = {h : [] for h in hexes}
    for i in range(0, parameter_graph.size()):
        zeb1_pitogether[GetHex.get_hex(i, parameter_graph)[0]].append(i)
        if not i%100000:
            print("parameter {}".format(i))

    json.dump(zeb1_pitogether,open("zeb1_layerdict.json","w"))

#Need code that combines lists into the right layers
d = json.load(open("zeb1_layerdict.json"))
zeb1_l1_pis = d['000000']
zeb1_l2_pis = d['200000']
zeb1_l3_pis = d['200200'] + d['240000'] + d['208000'] + d['600000']
zeb1_l4_pis = d['240200'] + d['208200'] + d['248000'] + d['600200'] + d['640000'] + d['608000'] + d['E00000']
zeb1_l5_pis = d['240240'] + d['248200'] + d['208208'] + d['249000'] + d['640200'] + d['600600'] + d['608200'] + d['E00200'] + d['6C0000'] + d['648000'] + d['E40000'] + d['618000'] + d['E08000']
zeb1_l6_pis = d['248240'] + d['248208'] + d['249200'] + d['640240'] + d['640600'] + d['608208'] + d['6C0200'] + d['648200'] + d['E40200'] + d['608600'] + d['E00600'] + d['E08200'] + d['618200'] \
                     + d['649000'] + d['6C8000'] + d['EC0000'] + d['658000'] + d['E48000'] + d['E18000'] 
zeb1_l7_pis = d['248248'] + d['249240'] + d['249208'] + d['648240'] + d['640640'] + d['6C0240'] + d['E40240'] + d['648208'] + d['6C0600'] + d['648600'] + d['E40600'] + d['608608'] + d['E08208'] \
                     + d['618208'] + d['649200'] + d['6C8200'] + d['EC0200'] + d['E48200'] + d['E00E00'] + d['E08600'] + d['618600'] + d['658200'] + d['E18200'] + d['6C9000'] + d['659000'] + d['E49000'] \
                     + d['FC0000'] + d['6D8000'] + d['EC8000'] + d['E58000'] + d['E38000']
zeb1_l8_pis = d['249248'] + d['648248'] + d['649240'] + d['648640'] + d['6C0640'] + d['6C8240'] + d['E48240'] + d['E40640'] + d['649208'] + d['EC0240'] + d['648608'] + d['6C8600'] + d['E48208'] \
                     + d['EC0600'] + d['E40E00'] + d['658208'] + d['E48600'] + d['E08608'] + d['618608'] + d['658600'] + d['E18208'] + d['6C9200'] + d['E49200'] + d['E08E00'] + d['659200'] + d['FC0200'] \
                     + d['EC8200'] + d['6D8200'] + d['E18600'] + d['E58200'] + d['E38200'] + d['6D9000'] + d['EC9000'] + d['E59000'] + d['FC8000'] + d['ED8000'] + d['E78000'] 
zeb1_l9_pis = d['249249'] + d['649248'] + d['648648'] + d['6C8640'] + d['6C06C0'] + d['E48248'] + d['6C9240'] + d['E49240'] + d['E48640'] + d['EC0640'] + d['EC8240'] + d['E40E40'] + d['E49208'] \
                     + d['659208'] + d['658608'] + d['FC0240'] + d['EC0E00'] + d['E48608'] + d['EC8600'] + d['618618'] + d['6D8600'] + d['FC0600'] + d['E48E00'] + d['E58208'] + d['E08E08'] + d['E18608'] \
                     + d['6D9200'] + d['E58600'] + d['E18E00'] + d['E38208'] + d['EC9200'] + d['E59200'] + d['FC8200'] + d['E38600'] + d['ED8200'] + d['E78200'] + d['6DB000'] + d['ED9000'] + d['FC9000'] \
                     + d['E79000'] + d['FD8000'] + d['EF8000']  
zeb1_l10_pis = d['649249'] + d['649648'] + d['6C9248'] + d['6C8648'] + d['6C86C0'] + d['E49248'] + d['659248'] + d['6C9640'] + d['658648'] + d['E48648'] + d['6D8640'] + d['EC06C0'] + d['EC8640'] \
                       + d['EC9240'] + d['E48E40'] + d['659608'] + d['6D9240'] + d['EC0E40'] + d['658618'] + d['6D8608'] + d['FC0640'] + d['6D9208'] + d['E59208'] + d['FC8240'] + d['FC0E00'] + d['EC8E00'] \
                       + d['E48E08'] + d['E58608'] + d['6D9600'] + d['FC8600'] + d['E18618'] + d['6DB200'] + d['E18E08'] + d['ED8600'] + d['E58E00'] + d['E78208'] + d['E38608'] + d['E38E00'] + d['ED9200'] \
                       + d['E78600'] + d['FC9200'] + d['E79200'] + d['FD8200'] + d['EF8200'] + d['EDB000'] + d['FD9000'] + d['EF9000'] + d['FF8000'] 
zeb1_l11_pis = d['649649'] + d['6C9249'] + d['659249'] + d['E49249'] + d['6C9648'] + d['6C86C8'] + d['6C96C0'] + d['E49648'] + d['6D86C0'] + d['659648'] + d['EC9248'] + d['6D8648'] + d['EC8648'] \
                       + d['EC86C0'] + d['6D9248'] + d['E59248'] + d['EC9640'] + d['658658'] + d['6D9640'] + d['E58648'] + d['E48E48'] + d['EC0EC0'] + d['659618'] + d['ED8640'] + d['6D8618'] + d['FC06C0'] \
                       + d['EC8E40'] + d['6D9608'] + d['E59608'] + d['ED9240'] + d['FC0E40'] + d['FC8640'] + d['FC9240'] + d['6DB240'] + d['E58618'] + d['6DB208'] + d['ED8608'] + d['ED9208'] + d['FC8E00'] \
                       + d['6DB600'] + d['E58E08'] + d['E18E18'] + d['ED8E00'] + d['E79208'] + d['E78608'] + d['E38618'] + d['E38E08'] + d['ED9600'] + d['FD8600'] + d['E78E00'] + d['EDB200'] + d['EF8600'] \
                       + d['FD9200'] + d['EF9200'] + d['FF8200'] + d['FDB000'] + d['EFB000'] + d['FF9000'] 
zeb1_l12_pis = d['FFB000'] + d['FF9200'] + d['EFB200'] + d['FDB200'] + d['FF8600'] + d['EF9600'] + d['FD9600'] + d['EF8E00'] + d['EDB600'] + d['EF9208'] + d['E38E18'] + d['EF8608'] + d['E78E08'] \
                       + d['FD8E00'] + d['EDB208'] + d['E78618'] + d['FD9240'] + d['EDB240'] + d['E79608'] + d['ED8E08'] + d['E58E18'] + d['ED9608'] + d['ED8618'] + d['6DB608'] + d['FD8640'] + d['FC8E40'] \
                       + d['ED8E40'] + d['E59618'] + d['E58E48'] + d['6DB640'] + d['FC9640'] + d['E79248'] + d['6DB248'] + d['FC86C0'] + d['FC0EC0'] + d['ED9640'] + d['6D9618'] + d['E58658'] + d['ED9248'] \
                       + d['EC8EC0'] + d['EC8E48'] + d['ED8648'] + d['FC9248'] + d['E59648'] + d['ED86C0'] + d['6D8658'] + d['E49E48'] + d['659658'] + d['EC96C0'] + d['6D9648'] + d['EC86C8'] + d['6D96C0'] \
                       + d['EC9648'] + d['6D86C8'] + d['6C96C8'] + d['E59249'] + d['EC9249'] + d['6D9249'] + d['E49649'] + d['659649'] + d['6C9649'] 
zeb1_l13_pis = d['6C96C9'] + d['6D9649'] + d['EC9649'] + d['659659'] + d['E49E49'] + d['E59649'] + d['6DB249'] + d['FC9249'] + d['ED9249'] + d['E79249'] + d['6D96C8'] + d['EC96C8'] + d['6D86D8'] \
                       + d['6D9658'] + d['ED86C8'] + d['EC9E48'] + d['FC9648'] + d['6DB6C0'] + d['ED96C0'] + d['E59658'] + d['ED9648'] + d['E59E48'] + d['EC8EC8'] + d['6DB648'] + d['ED8658'] + d['ED8EC0'] \
                       + d['FD9248'] + d['FC0FC0'] + d['FC96C0'] + d['FC8EC0'] + d['FD86C0'] + d['E79648'] + d['ED8E48'] + d['FC8E48'] + d['6DB618'] + d['FC9E40'] + d['E58E58'] + d['EDB248'] + d['EF9248'] \
                       + d['ED9618'] + d['EDB640'] + d['FD9640'] + d['FD8E40'] + d['E78E48'] + d['ED8E18'] + d['E79618'] + d['EDB608'] + d['E79E08'] + d['EF8618'] + d['E78E18'] + d['EF8E08'] + d['EF9608'] \
                       + d['FDB240'] + d['E38E38'] + d['EFB208'] + d['FF9240'] + d['FF8E00'] + d['FF9208'] + d['FDB600'] + d['EFB600'] + d['FF9600'] + d['FFB200'] + d['FFF000'] 
zeb1_l14_pis = d['6D96C9'] + d['EC96C9'] + d['6D9659'] + d['EC9E49'] + d['6DB649'] + d['FC9649'] + d['ED9649'] + d['E59659'] + d['E59E49'] + d['E79649'] + d['EDB249'] + d['FD9249'] + d['EF9249'] \
                       + d['6D96D8'] + d['6DB6C8'] + d['ED96C8'] + d['EC9EC8'] + d['FC96C8'] + d['6DB658'] + d['ED86D8'] + d['ED9658'] + d['ED9E48'] + d['E59E58'] + d['ED8EC8'] + d['FC9E48'] + d['EDB6C0'] \
                       + d['FD9648'] + d['FC8EC8'] + d['FC8FC0'] + d['FC9EC0'] + d['FD96C0'] + d['FD8EC0'] + d['E79658'] + d['EDB648'] + d['E79E48'] + d['ED8E58'] + d['FD8E48'] + d['EF9648'] + d['FDB248'] \
                       + d['EDB618'] + d['FD9E40'] + d['E78E58'] + d['EF8E48'] + d['EFB248'] + d['EF9618'] + d['E79E18'] + d['EF8E18'] + d['E78E38'] + d['FF9248'] + d['FDB640'] + d['FF8E40'] + d['EF9E08'] \
                       + d['EFB608'] + d['FF8E08'] + d['FF9640'] + d['FF9608'] + d['FFB240'] + d['FFB208'] + d['FF9E00'] + d['FFB600'] + d['FFF200'] 
zeb1_l15_pis = d['6D96D9'] + d['6DB6C9'] + d['ED96C9'] + d['EC9EC9'] + d['FC96C9'] + d['6DB659'] + d['ED9659'] + d['FC9E49'] + d['ED9E49'] + d['EDB649'] + d['FD9649'] + d['E59E59'] + d['E79659'] \
                       + d['E79E49'] + d['EF9649'] + d['FDB249'] + d['EFB249'] + d['FF9249'] + d['6DB6D8'] + d['ED96D8'] + d['EDB6C8'] + d['ED9EC8'] + d['FC9EC8'] + d['FD96C8'] + d['EDB658'] + d['ED9E58'] \
                       + d['ED8ED8'] + d['FD9E48'] + d['FC8FC8'] + d['FC9FC0'] + d['FD8EC8'] + d['FD8FC0'] + d['FD9EC0'] + d['EF9658'] + d['FDB6C0'] + d['E79E58'] + d['FDB648'] + d['FF8EC0'] + d['EF9E48'] \
                       + d['EFB648'] + d['EF8E58'] + d['E78E78'] + d['FF8E48'] + d['EFB618'] + d['E79E38'] + d['EF9E18'] + d['EF8E38'] + d['FF9648'] + d['FF8E18'] + d['FFB248'] + d['FF9E40'] + d['FF9E08'] \
                       + d['FFB640'] + d['FFB608'] + d['FFF240'] + d['FFF208'] + d['FFBE00'] + d['FFF600'] 
zeb1_l16_pis = d['6DB6D9'] + d['ED96D9'] + d['EDB6C9'] + d['ED9EC9'] + d['FC9EC9'] + d['FD96C9'] + d['EDB659'] + d['ED9E59'] + d['FD9E49'] + d['EF9659'] + d['FDB649'] + d['E79E59'] + d['EF9E49'] \
                       + d['EFB649'] + d['FF9649'] + d['FFB249'] + d['EDB6D8'] + d['ED9ED8'] + d['FC9FC8'] + d['FD9EC8'] + d['FDB6C8'] + d['FD8ED8'] + d['FD8FC8'] + d['FD9FC0'] + d['FDBEC0'] + d['FF8FC0'] \
                       + d['FF8EC8'] + d['EF8ED8'] + d['EFB658'] + d['EF9E58'] + d['E79E78'] + d['FF9EC0'] + d['EF8E78'] + d['FF9E48'] + d['FF8E58'] + d['FFB6C0'] + d['EFBE18'] + d['EF9E38'] + d['FF8E38'] \
                       + d['FFB648'] + d['FF9E18'] + d['FFB618'] + d['FFF248'] + d['FFBE40'] + d['FFBE08'] + d['FFF640'] + d['FFF608'] + d['FFFE00'] 
zeb1_l17_pis = d['6DB6DB'] + d['EDB6D9'] + d['ED9ED9'] + d['FD9EC9'] + d['FC9FC9'] + d['FDB6C9'] + d['EFB659'] + d['EF9E59'] + d['FF9E49'] + d['FFB649'] + d['EDBED8'] + d['FDB6D8'] + d['FD9ED8'] + d['FD9FC8'] \
               + d['FDBEC8'] + d['FD8FD8'] + d['E79E79'] + d['EFB6D8'] + d['FDBFC0'] + d['FF8FC8'] + d['EF9ED8'] + d['FF9FC0'] + d['FF9EC8'] + d['FF8ED8'] + d['EF8EF8'] + d['EFBE58'] + d['EF9E78'] \
               + d['FF9E58'] + d['FFB6C8'] + d['FFF249'] + d['FFBEC0'] + d['FF8E78'] + d['FFB658'] + d['EFBE38'] + d['FF9E38'] + d['FFBE48'] + d['FFF6C0'] + d['FFBE18'] + d['FFF648'] + d['FFFE40'] \
               + d['FFF618'] + d['FFFE08'] 
zeb1_l18_pis = d['EDB6DB'] + d['EDBED9'] + d['FDB6D9'] + d['FD9ED9'] + d['FD9FC9'] + d['FDBEC9'] + d['EFB6D9'] + d['EF9ED9'] + d['FF9EC9'] + d['EFBE59'] + d['FF9E59'] + d['FFB6C9'] + d['FFB659'] \
               + d['FFBE49'] + d['FDBED8'] + d['FD9FD8'] + d['FDBFC8'] + d['EF9E79'] + d['FF9FC8'] + d['FF8FD8'] + d['EFBED8'] + d['FF9ED8'] + d['FFB6D8'] + d['EF9EF8'] + d['FFBFC0'] + d['FFBEC8'] \
               + d['FF8EF8'] + d['EFBE78'] + d['FF9E78'] + d['FFF649'] + d['FFBE58'] + d['FFF6C8'] + d['FFFEC0'] + d['FFBE38'] + d['FFF658'] + d['FFFE48'] + d['FFFE18'] 
zeb1_l19_pis = d['EDBEDB'] + d['FDB6DB'] + d['EFB6DB'] + d['FDBED9'] + d['FD9FD9'] + d['FDBFC9'] + d['FF9FC9'] + d['EFBED9'] + d['FF9ED9'] + d['FFB6D9'] + d['FFBEC9'] + d['FFBE59'] + d['FDBFD8'] \
               + d['EF9EF9'] + d['EFBE79'] + d['FF9E79'] + d['FF9FD8'] + d['FFBFC8'] + d['FFBED8'] + d['FF8FF8'] + d['EFBEF8'] + d['FF9EF8'] + d['FFF6C9'] + d['FFF659'] + d['FFFE49'] + d['FFFFC0'] \
               + d['FFBE78'] + d['FFF6D8'] + d['FFFEC8'] + d['FFFE58'] + d['FFFE38'] 
zeb1_l20_pis = d['FDBEDB'] + d['EFBEDB'] + d['FFB6DB'] + d['FDBFD9'] + d['FF9FD9'] + d['FFBFC9'] + d['FFBED9'] + d['EFBEF9'] + d['FF9EF9'] + d['FFBE79'] + d['FFBFD8'] + d['FF9FF8'] + d['FFBEF8'] \
               + d['FFF6D9'] + d['FFFEC9'] + d['FFFE59'] + d['FFFFC8'] + d['FFFED8'] + d['FFFE78'] 
zeb1_l21_pis = d['FDBFDB'] + d['FFBEDB'] + d['EFBEFB'] + d['FFF6DB'] + d['FFBFD9'] + d['FF9FF9'] + d['FFBEF9'] + d['FFBFF8'] + d['FFFFC9'] + d['FFFED9'] + d['FFFE79'] + d['FFFFD8'] + d['FFFEF8'] 
zeb1_l22_pis = d['FFBFDB'] + d['FFBEFB'] + d['FFFEDB'] + d['FFBFF9'] + d['FFFFD9'] + d['FFFEF9'] + d['FFFFF8'] 
zeb1_l23_pis = d['FFBFFB'] + d['FFFFDB'] + d['FFFEFB'] + d['FFFFF9'] 
zeb1_l24_pis = d['FFFFFB'] 
zeb1_l25_pis = d['FFFFFF'] 


zeb1_layers = [zeb1_l1_pis, zeb1_l2_pis, zeb1_l3_pis, zeb1_l4_pis, zeb1_l5_pis, zeb1_l6_pis, zeb1_l7_pis, zeb1_l8_pis, zeb1_l9_pis, zeb1_l10_pis, zeb1_l11_pis, zeb1_l12_pis, zeb1_l13_pis, zeb1_l14_pis, zeb1_l15_pis, \
               zeb1_l16_pis, zeb1_l17_pis, zeb1_l18_pis, zeb1_l19_pis, zeb1_l20_pis, zeb1_l21_pis, zeb1_l22_pis, zeb1_l23_pis, zeb1_l24_pis, zeb1_l25_pis]