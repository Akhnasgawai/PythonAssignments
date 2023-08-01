"""3."""


def returnCharacters(string):
    if len(string) < 2:
        return "empty string"
    else:
        modified_string = string[0:2] + string[(len(string) - 2) : (len(string))]
        return modified_string


string = input("Enter the string: ")
print("{}".format(returnCharacters(string)))
