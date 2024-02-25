"""
Author: Antony S
Date: 2024-02-11
Program Name: Equilateral Triangle
Write a program that accepts the lengths of three sides of a triangle as inputs. 
The program output should indicate whether or not the triangle is an equilateral triangle
"""
print("Enter the three sides of a triangle")
x = int(input("1st side:"))
y = int(input("2nd side:"))
z = int(input("3rd side:"))

if x ==y and y==z:
    print("Equilateral Triangle")
else:
    print("Not equilateral Triangle")
