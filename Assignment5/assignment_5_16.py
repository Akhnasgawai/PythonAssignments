"""16"""
numbers = []
while True:
    num = input("Enter the number: ")
    if num == "q":
        break
    numbers.append(num)
num = input("Enter the number to delete: ")
if num in numbers:
    numbers.remove(num)
    print("Number deleted")
else:
    print("Number not found")
for number in numbers:
    print(number)
