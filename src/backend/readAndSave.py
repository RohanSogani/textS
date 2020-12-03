    import os
    import json
    import sys
    from collections import defaultdict

    ids_map = defaultdict()
    with open("id.txt") as ids:
        for l in ids:
            # print(l)
            l = l.strip()
            ids_map[str(l)] = True

    with open("train.txt") as train, open('new_train.txt', 'a') as the_file:
        for l in train:
            original_l = l
            split_l = l.split('\"article_id\"')
            id_raw = split_l[1].split(',')
            id_clean = id_raw[0].strip(':')
            id_clean = id_clean.strip('\"')
            if str(id_clean) in ids_map:
                the_file.write(l)


