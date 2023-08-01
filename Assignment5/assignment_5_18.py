"""17"""
odd = []
even = []
prime = []
for i in range(1, 101):
    if i == 1:
        prime.append(i)
        odd.append(i)
        continue
    if i % 2 == 0:
        even.append(i)
        if i == 2:
            prime.append(i)
        continue
    for j in range(2, int((i**0.5) + 1)):
        if i % j == 0:
            odd.append(i)
            break
    else:
        odd.append(i)
        prime.append(i)
print("prime: ", prime)
print("even: ", even)
print("odd: ", odd)

"""18"""
divisors = [4, 6, 8, 10, 3, 5, 7, 9]
divisible_by = {}
for divisor in divisors:
    divisible_by[divisor] = sorted(
        [num for num in even if num % divisor == 0]
        + [num for num in odd if num % divisor == 0]
    )

for divisor, numbers in divisible_by.items():
    print("Divisible by", divisor, ":", numbers)
