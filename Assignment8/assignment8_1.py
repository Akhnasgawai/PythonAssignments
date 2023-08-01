import random


def generate_random_number():
    digits = random.sample(range(10), 4)  # Sample 4 unique digits from 0 to 9
    if digits[0] == 0:
        digits[0], digits[1] = (
            digits[1],
            digits[0],
        )  # Ensure the first digit is not zero
    return str("".join(map(str, digits)))  # Join the digits and convert to integer


random_num = generate_random_number()
print(random_num)

# random_num = str(int(random.random() * 10000))
# print(random_num)
guess = 0
cows = 0
bulls = 0
while True:
    userInput = input("Guess a 4 digit number: ")
    guess += 1
    if userInput == random_num:
        print("Congratulations! You guessed the correct answer in", str(guess), "guess")
        break
    else:
        for i in range(4):
            if userInput[i] == random_num[i]:
                cows += 1
            elif userInput[i] in random_num:
                bulls += 1
        print("\nCows:", cows, "\tBulls:", bulls)
        cows = 0
        bulls = 0
