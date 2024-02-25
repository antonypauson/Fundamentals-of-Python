# Python program which calculates the square roots of numbers and comparing it with the Python Module's square root
#Using Newton's Algorithm for finding square root of a positive number
from math import sqrt
x = int(input("Enter the number:"))
z = 1.0
tolerance = 0.000001

while (True):
    z = (z + x / z) / 2
    diff = abs(x - z ** 2)
    if tolerance >= diff:
        break
print("Square Root = ",z)
print("Python's Estimate = ",sqrt(x))
# The program's estimate: 1.73205081001
# Python's estimate: 1.73205080757