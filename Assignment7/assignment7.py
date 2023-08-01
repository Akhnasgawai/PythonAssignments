"""2"""
# class Brackets:
#     def checkMatch(s):
#         li = []
#         for i in s:
#             if i in ["(", "{", "["]:
#                 li.append(i)
#             else:
#                 if i == "}" and li[-1] == "{":
#                     del li[-1]
#                 elif i == "]" and li[-1] == "[":
#                     del li[-1]
#                 elif i == ")" and li[-1] == "(":
#                     del li[-1]
#                 else:
#                     break
#         if li:
#             return "brackets does'nt match"
#         else:
#             return "brackets match"

# print(Brackets.checkMatch("(){}[]"))

"""3"""
# li = [4, 5, 6]
# class Subset:
#     def find_subset(nums):
#         subset = []
#         result = []

#         def dfs(i):
#             if i >= len(nums):
#                 result.append(subset.copy())
#                 return
#             subset.append(nums[i])
#             dfs(i + 1)
#             subset.pop()
#             dfs(i + 1)

#         dfs(0)
#         return result
# print(Subset.find_subset(li))

"""6"""
# class Math:
#     def power(x, n):
#         if n == 0:
#             return 1
#         if x == 0:
#             return 0
#         return x * Math.power(x, n - 1)

# print(Math.power(5, 3))

"""7"""
# class Reverse:
#     def reverse(s):
#         s2 = " "
#         s = s.split(" ")
#         s = s[::-1]
#         return s2.join(s)
# print(Reverse.reverse("hello .py"))

"""8"""
# class Play_string:
#     def get_string(self):
#         st = input("Enter the string: ")
#         self.st = st

#     def print_string(self):
#         return self.st[::-1]
# first_string = Play_string()
# first_string.get_string()
# print(first_string.print_string())

"""9"""
# class Circle:
#     pi = 3.14

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def area(self):
#         return self.pi * self.radius * self.radius

#     def perimeter(self):
#         return 2 * self.pi * self.radius

# circle_one = Circle(30)
# print(circle_one.area())
# print(circle_one.perimeter())

"""10"""
# class Calculator:
#     pass


# calculator_one = Calculator()
# print(calculator_one.__class__.__name__)
