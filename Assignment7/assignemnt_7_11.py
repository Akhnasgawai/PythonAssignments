"""1"""
# add = lambda x: x + 15
# multiply = lambda x, y: x * y
# print(add(5))
# print(multiply(5, 2))

"""2"""
# li = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
# sort = sorted(li, key=lambda x: x[1])
# print(sort)

"""3"""
# original_list = [
#     {"make": "Nokia", "model": 216, "color": "Black"},
#     {"make": "Mi Max", "model": 2, "color": "Gold"},
#     {"make": "Samsung", "model": 7, "color": "Blue"},
# ]

# sorted_list = sorted(original_list, key=lambda x: x["model"])
# print(sorted_list)

"""4"""
# st = "Hello"
# character = "H"
# res = lambda st, character: st.startswith(character)
# print(res(st, character))

"""5"""
# num = 9
# res = lambda num: num.isdigit()
# print(res(str(num)))

"""6"""
# original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# divisible = [num for num in original_list if num % 19 == 0 or num % 13 == 0]
# print(divisible)

"""7"""
# nested_lists = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# nested_lists = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# max_sum_list = sorted(nested_lists, key=lambda row: sum(row))
# print(max_sum_list)

"""8"""
# st = "PaceWisd0m"
# check = (
#     lambda st: any(char.isupper() for char in st)
#     and any(char.islower() for char in st)
#     and any(char.isdigit() for char in st)
#     and len(st) >= 10
# )

# print(check(st))

"""9"""
# original_list = ["red", "black", "white", "green", "orange"]
# search_string = "ack"
# check = [s for s in original_list if (lambda x: search_string in x)(s)]
# print(check)

"""10"""
# original_list = [19, "red", 12, "green", "blue", 10, "white", "green", 1]
# sorted_list = sorted(original_list, key=lambda x: (isinstance(x, str), x))
# print(sorted_list)
