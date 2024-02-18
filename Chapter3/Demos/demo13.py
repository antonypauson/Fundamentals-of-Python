# We can now use random.randint, selection, and a loop to develop a simple guessing 
# game. At start-up, the user enters the smallest number and the largest number in the 
# range. The computer then selects a number from this range. On each pass through the 
# loop, the user enters a number to attempt to guess the number selected by the computer. The program responds by saying “You’ve got it,” “Too large, try again,” or “Too 
# small, try again.” When the user finally guesses the correct number, the program congratulates him and tells him the total number of guesses

from random import randint
smallNo = int(input("Enter the smallest number:"))
largeNo = int(input("Enter the largest number:"))
realNo = randint(smallNo,largeNo) #a random number is generated

while True:
    guessNo = int(input("Enter your Guess: "))
    if guessNo < realNo:
        print("Too small, try again")
    elif guessNo > realNo:
        print("Too large, try again")
    elif guessNo == realNo:
        print("You've Got it! Congrats the number was ",guessNo)
        break
    else:
        print("The entered number is out of the range specified!")




