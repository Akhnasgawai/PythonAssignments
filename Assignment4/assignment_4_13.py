"""13"""


def stringStartsWith(string, startsWith):
    if string.startswith(startsWith):
        return True
    else:
        return False


string = input("Enter the string: ")
startsWith = input("Enter the character/s to check whether it starts with or not: ")
print("{}".format(stringStartsWith(string, startsWith)))
