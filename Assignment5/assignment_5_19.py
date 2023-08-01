"""19"""
mixed_list = ["apple", 42, 3.14, "banana", 123, 0.5, "cherry", 789, 2.71828]
integers = []
floats = []
strings = []
for item in mixed_list:
    if type(item) == str:
        strings.append(item)
    elif type(item) == int:
        integers.append(item)
    else:
        floats.append(item)
print(integers)
print(floats)
print(strings)
