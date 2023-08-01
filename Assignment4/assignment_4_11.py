"""11"""


def reverseString(string):
    if len(string) % 4 == 0:
        string = string[::-1]
    return string


string = input(
    "Enter the string to be reversed (length should be in multiple of 4 to be reversed): "
)
print("{}".format(reverseString(string)))
