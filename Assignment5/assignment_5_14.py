"""14"""
table = [24, 50, 29]
for number in table:
    for i in range(1, 11):
        print("{} * {} = {}".format(number, i, number * i))
    print("{}".format("-" * 15))
