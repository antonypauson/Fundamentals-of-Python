"""
Author: Antony S
Date: 2024-02-11
Program: km to nautical miles
Write a program that takes as input a number of kilometers and prints the corressponding number of nautical miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and 
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North 
Pole and the equator.
• A nautical mile is 1 minute of an arc.
"""
km = float(input("Enter the number of kilometers: "))
fraction_distance = km / 10_000
distance_between_poles = 90 * 60
nautical_miles = fraction_distance * distance_between_poles
print(f"{km} km equals {nautical_miles} nautical miles")