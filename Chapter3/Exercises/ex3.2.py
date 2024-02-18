# Assume that x refers to a number. Write a code segment that prints the number’s 
# absolute value without using Python’s abs function

x = int(input("Enter the number:"))
if x < 0:
    x = -x

print(x)
