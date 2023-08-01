"""9"""


def removeCharacter(string, index):
    string = string[0:index] + string[index + 1 :]
    return string


string = input("Enter the string: ")
index = int(input("Enter the index to be removed: "))
print("{}".format(removeCharacter(string, index)))
