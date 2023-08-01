"""2. count the number of characters (character frequency) in a string"""


def countCharacter(string):
    frequencyCount = {}
    for character in string:
        if character in frequencyCount:
            frequencyCount[character] += 1
        else:
            frequencyCount[character] = 1
    return frequencyCount


string = input("Enter the string: ")
print(countCharacter(string))
