"""1"""
my_dict = {0: 10, 1: 20, 2: 15, 3: 35, 4: 30}
sorted_asc_dict = sorted(my_dict.items(), key=lambda x: x[1])
sorted_desc_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_asc_dict)
print(sorted_desc_dict)
