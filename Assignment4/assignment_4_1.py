"""1. length of the string"""


def lengthOfString(string):
    sum = 0
    for i in string:
        sum += 1
    return sum


string = input("Enter the string: ")
print("length of string is {}".format(lengthOfString(string)))
