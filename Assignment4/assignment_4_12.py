"""12"""


def convertToUpper(string):
    count = 0
    for i in range(4):
        if string[i].isupper():
            count += 1
    if count >= 2:
        string = string.upper()
    return string


string = input("Enter the string: ")
print("{}".format(convertToUpper(string)))
