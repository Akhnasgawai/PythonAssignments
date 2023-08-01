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
