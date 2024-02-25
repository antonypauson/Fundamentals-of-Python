# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Lucky Sevens
# the amount of money that the player wants to put into the pot, and play the game 
# until the pot is empty. At that point, the program should print the number of 
# rolls it took to break the player, as well as maximum amount of money in the pot.
import random
amount = int(input("Enter the amount you want to put in:"))
count = 0
max_amount = amount
while amount > 0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    count += 1
    if dice1 + dice2 == 7:
        amount += 4
        print("SEVENS!")
    else: 
        amount -= 1
        print("LOST!")
    max_amount = max(max_amount,amount)
print("Count = ", count)
print("Max Amount = ",max_amount)