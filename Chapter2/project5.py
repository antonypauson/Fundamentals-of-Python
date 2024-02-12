"""
Author: Antony S
Date: 2024-02-11
Program: Momentum Calc
An object’s momentum is its mass multiplied by its velocity. Write a program 
that accepts an object’s mass (in kilograms) and velocity (in meters per second) as 
inputs and then outputs its momentum
"""
mass = float(input("Enter the mass of an object: "))
velocity = float(input("Enter the velocity of an object: "))
momentum = mass * velocity

print("Momentum = ",momentum)