# Assume that the variable myString refers to a string. Write a code segment that uses a loop to print the characters of the string in reverse order.

myString = "Pulp Fiction"
for i in range(len(myString)-1,-1,-1):
    print(myString[i],end="")