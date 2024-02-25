# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Bouncing Ball

intialHeight = int(input("Enter the height:"))
bounceTimes = int(input("Enter no of bounces:"))
total_distance = 0
currentHeight = intialHeight

for i in range(bounceTimes + 1):
    total_distance += currentHeight
    currentHeight *= 0.6
    