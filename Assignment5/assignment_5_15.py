"""15"""
count = 0
sum = 0
product = 1
while True:
    num = input("Enter the number: ")
    if num == "q":
        break
    count += 1
    sum += int(num)
    product *= int(num)
print("Average of numbers are: ", sum / count)
print("Product of numbers are: ", product)
