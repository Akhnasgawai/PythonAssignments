"""6"""


def replaceEnds(string):
    if len(string) < 3:
        return string
    else:
        if string.endswith("ing"):
            string += "ly"
        else:
            string += "ing"
        return string


string = input("Enter the string: ")
print("{}".format(replaceEnds(string)))
