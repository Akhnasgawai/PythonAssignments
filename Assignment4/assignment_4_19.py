"""19"""


def maxAndMin(string):
    minLen = min([i for i in string.split()], key=len)
    maxLen = max([i for i in string.split()], key=len)
    return minLen, maxLen


string = input("Enter the string: ")
smallestWord, largestWord = maxAndMin(string)
print(
    'The smallest word is "{}" and the largest word is "{}"'.format(
        smallestWord, largestWord
    )
)
