#  Assume that the variable myString refers to a string, and the variable reversedString refers to an empty string. Write a loop that adds the characters from myString to reversedString in reverse order

myString = "Pulp Fiction"
reversedString = ""
for i in range(len(myString)-1,-1,-1):
    reversedString += myString[i]
print(reversedString)
