"""
Author: Antony S
Date: 2024-02-11
Program: Light Year Calc
Light travels at 3 *108
 meters per second. A light-year is the distance a light beam 
travels in one year. Write a program that calculates and displays the value of a 
light-yearLight travels at 3 *108
 meters per second. A light-year is the distance a light beam 
travels in one year. Write a program that calculates and displays the value of a 
light-year
"""
SPEED_OF_LIGHT_PER_SECOND = 3 * 10 ** 8
LightYear = SPEED_OF_LIGHT_PER_SECOND * 60 * 60 * 24 * 365
print("Light Year = ",LightYear)
#print(f"{LightYear:e}")