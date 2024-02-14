# Assume that the variable teststring refers to a string. Write a loop that prints 
# each character in this string, followed by its ASCII value.

teststring = input("Enter the string: ")
for x in teststring: 
    print(f"{x} has ASCII of ",ord(x))