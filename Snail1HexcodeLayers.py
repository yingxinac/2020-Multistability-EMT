# Snail1HexcodeLayers.py
# MIT LICENSE 2016


#Get the list of ParameterIndices of each Snail1 hexcode layer.

import DSGRN
import GetHex
import Snail1hexcodeijk_pitogether
database = DSGRN.Query.Database.Database("EMT_Snail1notE.db")
parameter_graph = database.parametergraph

#Get the list of Snail1 hexcodes for all ParameterIndices.
all_hexonly_snail1 = []
for k in range(0, parameter_graph.size()):
    all_hexonly_snail1.append('*')

for i in range(0, parameter_graph.size()):
    all_hexonly_snail1[i] = GetHex.get_hex(i, parameter_graph)[1]

#Get the list of ParamerIndices with Sanil1 hexcode being 'ijk':
snail1000_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '000',all_hexonly_snail1)

snail1FFF_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FFF',all_hexonly_snail1)

snail1200_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '200',all_hexonly_snail1)

snail1208_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '208',all_hexonly_snail1)

snail1240_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '240',all_hexonly_snail1)

snail1600_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '600',all_hexonly_snail1)

snail1248_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '248',all_hexonly_snail1)

snail1608_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '608',all_hexonly_snail1)

snail1640_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '640',all_hexonly_snail1)

snail1E00_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E00',all_hexonly_snail1)

snail1249_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '249',all_hexonly_snail1)

snail1648_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '648',all_hexonly_snail1)

snail1618_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '618',all_hexonly_snail1)

snail16C0_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6C0',all_hexonly_snail1)

snail1E08_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E08',all_hexonly_snail1)

snail1E40_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E40',all_hexonly_snail1)

snail1649_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '649',all_hexonly_snail1)

snail1658_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '658',all_hexonly_snail1)

snail16C8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6C8',all_hexonly_snail1)

snail1E48_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E48',all_hexonly_snail1)

snail1E18_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E18',all_hexonly_snail1)

snail1EC0_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EC0',all_hexonly_snail1)

snail1659_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '659',all_hexonly_snail1)

snail16C9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6C9',all_hexonly_snail1)

snail16D8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6D8',all_hexonly_snail1)

snail1E49_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E49',all_hexonly_snail1)

snail1E58_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E58',all_hexonly_snail1)

snail1EC8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EC8',all_hexonly_snail1)

snail1E38_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E38',all_hexonly_snail1)

snail1FC0_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FC0',all_hexonly_snail1)

snail16D9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6D9',all_hexonly_snail1)

snail1E59_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E59',all_hexonly_snail1)

snail1EC9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EC9',all_hexonly_snail1)

snail1ED8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'ED8',all_hexonly_snail1)

snail1E78_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E78',all_hexonly_snail1)

snail1FC8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FC8',all_hexonly_snail1)

snail16DB_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    '6DB',all_hexonly_snail1)

snail1ED9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'ED9',all_hexonly_snail1)

snail1E79_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'E79',all_hexonly_snail1)

snail1EF8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EF8',all_hexonly_snail1)

snail1FC9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FC9',all_hexonly_snail1)

snail1FD8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FD8',all_hexonly_snail1)

snail1EDB_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EDB',all_hexonly_snail1)

snail1EF9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EF9',all_hexonly_snail1)

snail1FD9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FD9',all_hexonly_snail1)

snail1FF8_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FF8',all_hexonly_snail1)

snail1EFB_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'EFB',all_hexonly_snail1)

snail1FDB_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FDB',all_hexonly_snail1)

snail1FF9_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FF9',all_hexonly_snail1)

snail1FFB_pitogether = Snail1hexcodeijk_pitogether.snail1ijk_pitogether(
    'FFB',all_hexonly_snail1)

#Get the list of ParameterIndices of each Snail1 hexcode layer.
snail1_l1_pis = snail1000_pitogether
snail1_l2_pis = snail1200_pitogether
snail1_l3_pis = snail1208_pitogether + snail1240_pitogether + \
                snail1600_pitogether
snail1_l4_pis = snail1248_pitogether + snail1608_pitogether + \
                snail1640_pitogether + \
                   snail1E00_pitogether
snail1_l5_pis = snail1249_pitogether + snail1648_pitogether + \
                snail1618_pitogether + \
                   snail16C0_pitogether + snail1E08_pitogether + snail1E40_pitogether
snail1_l6_pis = snail1649_pitogether + snail1658_pitogether + \
                snail16C8_pitogether + \
                   snail1E48_pitogether + snail1E18_pitogether + snail1EC0_pitogether
snail1_l7_pis = snail1659_pitogether + snail16C9_pitogether + \
                snail16D8_pitogether + \
                   snail1E49_pitogether + snail1E58_pitogether + snail1EC8_pitogether + \
                   snail1E38_pitogether + snail1FC0_pitogether
snail1_l8_pis = snail16D9_pitogether + snail1E59_pitogether + \
                snail1EC9_pitogether + \
                   snail1ED8_pitogether + snail1E78_pitogether + snail1FC8_pitogether
snail1_l9_pis = snail16DB_pitogether + snail1ED9_pitogether + \
                snail1E79_pitogether + \
                   snail1EF8_pitogether + snail1FC9_pitogether + snail1FD8_pitogether
snail1_l10_pis = snail1EDB_pitogether + snail1EF9_pitogether + \
                 snail1FD9_pitogether + \
                    snail1FF8_pitogether
snail1_l11_pis = snail1EFB_pitogether + snail1FDB_pitogether + \
                 snail1FF9_pitogether
snail1_l12_pis = snail1FFB_pitogether
snail1_l13_pis = snail1FFF_pitogether

snail1_layers = [snail1_l1_pis,
                           snail1_l2_pis,
                           snail1_l3_pis,
                           snail1_l4_pis,
                           snail1_l5_pis,
                           snail1_l6_pis,
                           snail1_l7_pis,
                           snail1_l8_pis,
                           snail1_l9_pis,
                           snail1_l10_pis,
                           snail1_l11_pis,
                           snail1_l12_pis,
                           snail1_l13_pis]