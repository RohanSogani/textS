import os
import json

with open('cd.json') as data_file:
    for l in data_file:
        # get ids and clean ";,etc"
        split_l = l.split('\"id\"')
        id_raw = split_l[1].split(',')
        id_clean = id_raw[0].strip(':')
        id_clean = id_clean.strip('\"')
        print(id_clean)
        # create url and curl download command
        url = "https://arxiv.org/pdf/" + str(id_clean) + ".pdf"
        dl_cmd = "curl -O " + url
        os.system(dl_cmd)