"""1"""
# for num in range(1500, 2701):
#     if num % 7 == 0 and num % 5 == 0:
#         print(num)

"""2"""
# for num in range(0, 7):
#     if num == 3 or num == 6:
#         continue
#     print(num)

"""3"""
# for num in range(0, 6):
#     if num % 5 == 0 and num % 3 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print("buzz")
#     else:
#         print(num)

"""4"""
# x = 6
# y = 8
# z = 12
# if x == y == z:
#     print("Equilateral Triangle")
# elif x == y or y == z or z == x:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

"""5"""
# numbers = []
# sum = 0
# while True:
#     num = int(input("Enter the number or (0) to quit : "))
#     if num == 0:
#         break
#     numbers.append(num)
# for num in numbers:
#     sum += num
# average = sum / len(numbers)
# print("Sum ", sum)
# print("Average ", average)

"""6"""
# for i in range(10):
#     for j in range(i):
#         print(i, end="")
#     print("")

"""7"""
# l = [10, 20, 30, 40, 50, 20, 21, 22, 40]
# count = 0
# for i in l:
#     if i > 30:
#         count += 1
# print(count)

"""8"""
# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))
# if length == breadth:
#     print("It is a square")
# else:
#     print("It is not a square")

"""9"""
# quantity = int(input("Enter the quantity: "))
# price = quantity * 100
# if price > 1000:
#     discount = price * 0.1
#     price -= discount
# print(price)

"""10"""
# salary = int(input("Enter your salary: "))
# year = int(input("Enter the total no years you served the company: "))
# if year > 5:
#     bonus = salary * 0.05
#     salary += bonus
# print("Net Salary after bonus: ", salary)

"""11"""
# marks = int(input("Enter the marks: "))
# if marks < 25:
#     print("F")
# elif marks >= 25 and marks < 45:
#     print("E")
# elif marks >= 45 and marks < 50:
#     print("D")
# elif marks >= 50 and marks < 60:
#     print("C")
# elif marks >= 60 and marks < 80:
#     print("B")
# else:
#     print("A")

"""12"""
# class_held = int(input("Enter the total number of classes held: "))
# class_attended = int(input("Enter the number of classes attended: "))
# percentage = (class_attended / class_held) * 100
# print(percentage)
# if percentage < 75:
#     print("Not allowed to sit for exam")
# else:
#     print("Allowed to sit for exam")

"""13"""
# i = 0
# sum = 0
# while i < 10:
#     num = int(input("Enter the number: "))
#     sum += num
#     i += 1
# print("Average of numbers are: ", sum / 10)

"""14"""
# table = [24, 50, 29]
# for number in table:
#     for i in range(1, 11):
#         print("{} * {} = {}".format(number, i, number * i))
#     print("{}".format("-" * 15))

"""15"""
# count = 0
# sum = 0
# product = 1
# while True:
#     num = input("Enter the number: ")
#     if num == "q":
#         break
#     count += 1
#     sum += int(num)
#     product *= int(num)
# print("Average of numbers are: ", sum / count)
# print("Product of numbers are: ", product)

"""16"""
# numbers = []
# while True:
#     num = input("Enter the number: ")
#     if num == "q":
#         break
#     numbers.append(num)
# num = input("Enter the number to delete: ")
# if num in numbers:
#     numbers.remove(num)
#     print("Number deleted")
# else:
#     print("Number not found")
# for number in numbers:
#     print(number)

"""17"""
# odd = []
# even = []
# prime = []
# for i in range(1, 101):
#     if i == 1:
#         prime.append(i)
#         odd.append(i)
#         continue
#     if i % 2 == 0:
#         even.append(i)
#         if i == 2:
#             prime.append(i)
#         continue
#     for j in range(2, int((i**0.5) + 1)):
#         if i % j == 0:
#             odd.append(i)
#             break
#     else:
#         odd.append(i)
#         prime.append(i)
# print("prime: ", prime)
# print("even: ", even)
# print("odd: ", odd)

"""18"""
# divisors = [4, 6, 8, 10, 3, 5, 7, 9]
# divisible_by = {}
# for divisor in divisors:
#     divisible_by[divisor] = sorted(
#         [num for num in even if num % divisor == 0]
#         + [num for num in odd if num % divisor == 0]
#     )

# for divisor, numbers in divisible_by.items():
#     print("Divisible by", divisor, ":", numbers)

"""19"""
# mixed_list = ["apple", 42, 3.14, "banana", 123, 0.5, "cherry", 789, 2.71828]
# integers = []
# floats = []
# strings = []
# for item in mixed_list:
#     if type(item) == str:
#         strings.append(item)
#     elif type(item) == int:
#         integers.append(item)
#     else:
#         floats.append(item)
# print(integers)
# print(floats)
# print(strings)

"""20"""
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squares = [num * num for num in numbers]
# print(squares)
