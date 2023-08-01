"""12"""
class_held = int(input("Enter the total number of classes held: "))
class_attended = int(input("Enter the number of classes attended: "))
percentage = (class_attended / class_held) * 100
print(percentage)
if percentage < 75:
    print("Not allowed to sit for exam")
else:
    print("Allowed to sit for exam")
