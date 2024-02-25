# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Guessing Game
# A program where the computer have to guess the number user have given. The user puts a feedback saying if it was high or low or correct. The computer randomnly guesses it by adjusting the smaller and larger range of random.randint() function.
import random
smaller = 1
larger = 50
realNumber = int(input("Enter the number computer have to guess:"))
minimumGuess = 20
while minimumGuess > 0:
    computerGuess = random.randint(smaller,larger)
    print(computerGuess)
    minimumGuess -= 1
    feedback = input("[high],[low],[yes]")

    if feedback.lower() == "high" and computerGuess > realNumber:
        larger = computerGuess - 1
    elif feedback.lower() == "low" and computerGuess < realNumber:
        smaller = computerGuess + 1
    elif feedback.lower() == "yes":
        print("Computer Guessed it")
        break

    if minimumGuess <= 0:
        print("No. of attempts have ended!")
