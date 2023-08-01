"""16"""


def findIndex(string, character):
    try:
        index = string.index(character)
        return index
    except ValueError:
        return None


string = input("Enter the string: ")
character = input("Enter the character to be find: ")
print("character {} is at index {}".format(character, findIndex(string, character)))
