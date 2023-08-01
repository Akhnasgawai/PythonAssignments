"""7"""


def replaceSentence(string):
    index_not = string.find("not")
    index_poor = string.find("poor")
    if index_not < index_poor and index_not != -1 and index_poor != -1:
        string = string[0:index_not] + "good!"
        return string
    else:
        return string


string = input("Enter the string: ")
print("{}".format(replaceSentence(string)))
