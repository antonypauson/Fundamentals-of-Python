"""
Author: Antony S
Date: 2024-02-11
Program: KE
 The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
where m is the object’s mass and v is its velocity. Modify the program you created 
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.
"""
mass = float(input("Enter the mass of an object: "))
velocity = float(input("Enter the velocity of an object: "))
momentum = mass * velocity
kineticEnery = 0.5 * mass * velocity ** 2
print("Momentum = ",momentum)
print("Kinetic Energy = ", kineticEnery)