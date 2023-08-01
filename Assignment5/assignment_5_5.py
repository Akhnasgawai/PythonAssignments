"""5"""
numbers = []
sum = 0
while True:
    num = int(input("Enter the number or (0) to quit : "))
    if num == 0:
        break
    numbers.append(num)
for num in numbers:
    sum += num
average = sum / len(numbers)
print("Sum ", sum)
print("Average ", average)
