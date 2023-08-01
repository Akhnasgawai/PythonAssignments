"""4. replace all the occurrences of first string, except the first string itself"""


def replaceCharacter(string):
    if len(string) < 2:
        return string
    else:
        first_char = string[0]
        modified_string = first_char + string[1:].replace(first_char, "$")
        return modified_string


string = input("Enter the string: ")
print("{}".format(replaceCharacter(string)))
