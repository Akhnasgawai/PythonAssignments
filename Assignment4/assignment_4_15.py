"""15"""


def countAboveOne(string):
    countingFrequency = {}
    for key in string:
        if key in countingFrequency:
            countingFrequency[key] += 1
        else:
            countingFrequency[key] = 1
    for key in countingFrequency:
        if countingFrequency[key] != 1:
            print(key, " ", countingFrequency[key])


string = "thequickbrownfoxjumpsoverthelazydog"
countAboveOne(string)
