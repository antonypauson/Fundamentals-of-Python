"""
Author: Antony S
Date: 2024-02-11
Program: Rent Calculator
Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who 
like to buy LP record albums. The store rents new videos for $3.00 a night, and 
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video 
can use to calculate the total charge for a customer’s video rentals. The program 
should prompt the user for the number of each type of video and output the total 
cost"""
NEW_VIDEOS = 3.00
OLD_VIDEOS = 2.00
noOldVideo = int(input("Enter the no. of Old Video Rentals: "))
noNewVideo = int(input("Enter the no. of New Video Rentals: "))

totalCharge = noOldVideo * OLD_VIDEOS + noNewVideo * NEW_VIDEOS
print(f"${totalCharge}")