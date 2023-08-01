"""1"""
# my_dict = {0: 10, 1: 20, 2: 15, 3: 35, 4: 30}
# sorted_asc_dict = sorted(my_dict.items(), key=lambda x: x[1])
# sorted_desc_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# print(sorted_asc_dict)
# print(sorted_desc_dict)

"""2"""
# my_dict = {0: 10, 1: 0}
# my_dict[2] = 30
# print(my_dict)

"""3"""
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = dic1 | dic2 | dic3
# print(dic4)

"""4"""
# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = 1
# if key in my_dict:
#     print("true")
# else:
#     print("false")

"""5"""
# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for key, values in my_dict.items():
#     print(key, "->", values)

"""6"""
# number = int(input("Enter the number: "))
# my_dict = {}
# for i in range(number):
#     my_dict[i + 1] = (i + 1) * (i + 1)
# print(my_dict)

"""7"""
# dict_1 = {1: "a", 2: "b"}
# dict_2 = {3: "c", 4: "d"}
# print(dict_1 | dict_2)

"""8"""
# dict_1 = {"a": 100, "b": 200, "c": 300}
# sum = 0
# for val in dict_1.values():
#     sum += val
# print(sum)

"""9"""
# dict_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
# mul = 1
# for val in dict_1.values():
#     mul *= val
# print(mul)

"""10"""
# dic1 = {1: 10, 2: 20}
# dic1.pop(2)
# print(dic1)

"""11"""
# my_dict = {5: 10, 4: 20, 6: 15, 13: 35, 8: 30}
# sorted_by_key = dict(sorted(my_dict.items()))
# print(sorted_by_key)

"""12"""
# my_dict = {5: 10, 4: 20, 6: 15, 13: 35, 8: 30}
# max_value = max(sorted(my_dict.values()))
# print(max_value)

"""13"""
# d1 = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1}
# d1 = {val: key for key, val in d1.items()}
# d1 = {val: key for key, val in d1.items()}
# print(d1)

"""14"""
# my_dict = {}
# if my_dict:
#     print("Not empty")
# else:
#     print("empty")

"""15"""
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 300, "b": 200, "d": 400}
# d3 = {}
# for key, value in d1.items():
#     if key in d2:
#         d3.update({key: value + d2[key]})
#     else:
#         d3.update({key: value})
# for key, value in d2.items():
#     if key not in d3:
#         d3.update({key: value})
# print(d3)

"""16"""
# d1 = {"a": 1, "b": 2, "c": 5, "d": 8, "e": 3, "f": 7}
# d2 = sorted(d1.values())
# print(d2[-3:])

"""17"""
# d1 = {"key1": 1, "key2": 1, "key3": 2}
# d2 = {"key1": 1, "key2": 2}

# for item in d1:
#     if item in d2:
#         if d1[item] == d2[item]:
#             print("{} : {} is present in both d1 and d2".format(item, d1[item]))

"""18"""
# li = [{}, {}, {}]
# empty = True
# for i in li:
#     if i:
#         empty = False
#         break
#     else:
#         continue
# if empty:
#     print("All the dictionaries in list are empty")
# else:
#     print("Dictionaries in the list contains items")

"""19"""
# li = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# li2 = []
# for i in li:
#     if i in li2:
#         li.remove(i)
#     else:
#         li2.append(i)
# print(li)

"""20"""
# l1 = [10, 20, 30]
# l2 = [40, 50, 60]
# print(l2 + l1)
