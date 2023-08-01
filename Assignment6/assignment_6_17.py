"""17"""
d1 = {"key1": 1, "key2": 1, "key3": 2}
d2 = {"key1": 1, "key2": 2}

for item in d1:
    if item in d2:
        if d1[item] == d2[item]:
            print("{} : {} is present in both d1 and d2".format(item, d1[item]))
