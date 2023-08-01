"""18"""
li = [{}, {}, {}]
empty = True
for i in li:
    if i:
        empty = False
        break
    else:
        continue
if empty:
    print("All the dictionaries in list are empty")
else:
    print("Dictionaries in the list contains items")
