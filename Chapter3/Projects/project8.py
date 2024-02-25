# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Greatest Common Divisor using Euclid's Algorithm

A = int(input("Enter first number: "))
B = int(input("Enter second number:"))
numbers = sorted([A,B])
larger = numbers[1]
smaller = numbers[0]
# print(larger,smaller)
rem = 0
while smaller > 0:
    rem = larger % smaller
    larger = smaller
    smaller = rem
print(larger)
