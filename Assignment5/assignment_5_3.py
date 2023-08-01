"""3"""
for num in range(0, 6):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
