"""15"""
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
d3 = {}
for key, value in d1.items():
    if key in d2:
        d3.update({key: value + d2[key]})
    else:
        d3.update({key: value})
for key, value in d2.items():
    if key not in d3:
        d3.update({key: value})
print(d3)
