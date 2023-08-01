"""8"""


def longestString(li):
    maxLen = max([len(i) for i in li])
    return maxLen


listOfStrings = ["abc", "abcde", "abcd", "abcdefgh"]
print("Length of longest string in list is {}".format(longestString(listOfStrings)))
