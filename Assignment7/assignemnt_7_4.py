"""4"""
numbers = [90, 20, 10, 40, 50, 60, 70]
target = 60
for number in numbers:
    for num in numbers[(numbers.index(number)) :]:
        if number + num == target:
            print(numbers.index(number), " : ", numbers.index(num))
            break
