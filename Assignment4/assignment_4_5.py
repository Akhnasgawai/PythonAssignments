"""5"""


def mergeAndReplace(string1, string2):
    modified_string = string2[0:2] + string1[2:] + " " + string1[0:2] + string2[2:]
    return modified_string


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("{}".format(mergeAndReplace(string1, string2)))
