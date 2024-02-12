"""
Author: Antony S
Date: 2024-02-11
Program: Show sphere's dimensions
Write a program that takes the radius of a sphere (a floating-point number) as 
input and then outputs the sphere’s diameter, circumference, surface area, and 
volume.
"""
from math import pi
radius = float(input("Enter the radius of Sphere:"))
diameter = radius * 2
circumference = 2 * pi * radius
sArea = 4 * pi * radius ** 2
vol = 4 / 3 * pi * radius ** 3
print("Radius = ", radius) 
print("Diameter = ", diameter)
print("Surface Area = ", sArea)
print("Volume = ", vol)
