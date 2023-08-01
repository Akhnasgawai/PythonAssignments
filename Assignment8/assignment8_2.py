# import random

# with open("hangman.txt", "r") as f:
#     content = [line.strip() for line in f.readlines()]


# def getRandomWord(content):
#     print(len(content))
#     index = int(random.uniform(0, len(content)))
#     print(content[index])


# getRandomWord(content)

word = "EVAPORATE"
guess = 6
letters_guessed = []
hidden = "_" * len(word)
print(hidden)
while guess:
    letter = input("Enter the letter to be guessed: ")
    if letter in letters_guessed:
        print("Letter already guessed, try again")
        continue
    letters_guessed.append(letter)
    if letter not in word:
        guess -= 1
        print("Incorrect!")
        print("You left with {} chances to guess".format(guess))
        continue
    # print(guess)
    indices = []
    for index in range(len(word)):
        if word[index] == letter:
            hidden = hidden[:index] + letter + hidden[index + 1 :]
            indices.append(index)
    print(hidden)
    if "_" not in hidden:
        break

if "_" in hidden:
    print("You lost, the word was {}".format(word))
else:
    print(
        "Yay !! You won!!, You guesses the words in {} chances!".format(
            len(letters_guessed)
        )
    )
