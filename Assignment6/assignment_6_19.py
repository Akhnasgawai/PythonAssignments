"""19"""
li = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
li2 = []
for i in li:
    if i in li2:
        li.remove(i)
    else:
        li2.append(i)
print(li)
