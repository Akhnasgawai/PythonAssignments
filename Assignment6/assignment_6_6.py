"""6"""
number = int(input("Enter the number: "))
my_dict = {}
for i in range(number):
    my_dict[i + 1] = (i + 1) * (i + 1)
print(my_dict)
