"""4"""
x = 6
y = 8
z = 12
if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
