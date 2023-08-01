"""1. length of the string"""
# def lengthOfString(string):
#     sum = 0
#     for i in string:
#         sum += 1
#     return sum
# string = input("Enter the string: ")
# print("length of string is {}".format(lengthOfString(string)))

"""2. count the number of characters (character frequency) in a string"""
# def countCharacter(string):
#     frequencyCount = {}
#     for character in string:
#         if character in frequencyCount:
#             frequencyCount[character] += 1
#         else:
#             frequencyCount[character] = 1
#     return frequencyCount
# string = input("Enter the string: ")
# print(countCharacter(string))

"""3."""
# def returnCharacters(string):
#     if len(string) < 2:
#         return "empty string"
#     else:
#         modified_string = string[0:2] + string[(len(string) - 2) : (len(string))]
#         return modified_string
# string = input("Enter the string: ")
# print("{}".format(returnCharacters(string)))

"""4. replace all the occurrences of first string, except the first string itself"""
# def replaceCharacter(string):
#     if len(string) < 2:
#         return string
#     else:
#         first_char = string[0]
#         modified_string = first_char + string[1:].replace(first_char, "$")
#         return modified_string
# string = input("Enter the string: ")
# print("{}".format(replaceCharacter(string)))

"""5"""
# def mergeAndReplace(string1, string2):
#     modified_string = string2[0:2] + string1[2:] + " " + string1[0:2] + string2[2:]
#     return modified_string
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# print("{}".format(mergeAndReplace(string1, string2)))

"""6"""
# def replaceEnds(string):
#     if len(string) < 3:
#         return string
#     else:
#         if string.endswith("ing"):
#             string += "ly"
#         else:
#             string += "ing"
#         return string
# string = input("Enter the string: ")
# print("{}".format(replaceEnds(string)))

"""7"""
# def replaceSentence(string):
#     index_not = string.find("not")
#     index_poor = string.find("poor")
#     if index_not < index_poor and index_not != -1 and index_poor != -1:
#         string = string[0:index_not] + "good!"
#         return string
#     else:
#         return string
# string = input("Enter the string: ")
# print("{}".format(replaceSentence(string)))

"""8"""
# def longestString(li):
#     maxLen = max([len(i) for i in li])
#     return maxLen
# listOfStrings = ["abc", "abcde", "abcd", "abcdefgh"]
# print("Length of longest string in list is {}".format(longestString(listOfStrings)))

"""9"""
# def removeCharacter(string, index):
#     string = string[0:index] + string[index + 1 :]
#     return string
# string = input("Enter the string: ")
# index = int(input("Enter the index to be removed: "))
# print("{}".format(removeCharacter(string, index)))

"""10"""
# def unique_words(string):
#     words = string.split(", ")
#     unique = sorted(set(words))
#     return ", ".join(unique)
# string = "red, white, black, red, green, black"
# print("{}".format(unique_words(string)))

"""11"""
# def reverseString(string):
#     if len(string) % 4 == 0:
#         string = string[::-1]
#     return string
# string = input(
#     "Enter the string to be reversed (length should be in multiple of 4 to be reversed): "
# )
# print("{}".format(reverseString(string)))

"""12"""
# def convertToUpper(string):
#     count = 0
#     for i in range(4):
#         if string[i].isupper():
#             count += 1
#     if count >= 2:
#         string = string.upper()
#     return string
# string = input("Enter the string: ")
# print("{}".format(convertToUpper(string)))

"""13"""
# def stringStartsWith(string, startsWith):
#     if string.startswith(startsWith):
#         return True
#     else:
#         return False
# string = input("Enter the string: ")
# startsWith = input("Enter the character/s to check whether it starts with or not: ")
# print("{}".format(stringStartsWith(string, startsWith)))

"""14"""
# pi = 3.1415926
# print("{:.2f}".format(pi))

"""15"""
# def countAboveOne(string):
#     countingFrequency = {}
#     for key in string:
#         if key in countingFrequency:
#             countingFrequency[key] += 1
#         else:
#             countingFrequency[key] = 1
#     for key in countingFrequency:
#         if countingFrequency[key] != 1:
#             print(key, " ", countingFrequency[key])
# string = "thequickbrownfoxjumpsoverthelazydog"
# countAboveOne(string)

"""16"""
# def findIndex(string, character):
#     try:
#         index = string.index(character)
#         return index
#     except ValueError:
#         return None
# string = input("Enter the string: ")
# character = input("Enter the character to be find: ")
# print("character {} is at index {}".format(character, findIndex(string, character)))

"""17"""
# s = "a b c"
# s = s.split()
# print(s)

"""18"""
# s = "32.054,23"
# s = s.replace(".", "#").replace(",", ".").replace("#", ",")
# print(s)

"""19"""
# def maxAndMin(string):
#     minLen = min([i for i in string.split()], key=len)
#     maxLen = max([i for i in string.split()], key=len)
#     return minLen, maxLen
# string = input("Enter the string: ")
# smallestWord, largestWord = maxAndMin(string)
# print(
#     'The smallest word is "{}" and the largest word is "{}"'.format(
#         smallestWord, largestWord
#     )
# )

"""20"""
# s = "the fox the were fox"
# s = set(s.split())
# print(" ".join(s))
