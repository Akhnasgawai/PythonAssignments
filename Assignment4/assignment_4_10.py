"""10"""


def unique_words(string):
    words = string.split(", ")
    unique = sorted(set(words))
    return ", ".join(unique)


string = "red, white, black, red, green, black"
print("{}".format(unique_words(string)))
