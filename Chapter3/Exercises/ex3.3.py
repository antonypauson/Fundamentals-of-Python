# Write a loop that counts the number of space characters in a string. Recall that the 
# space character is represented as ' '
count = 0
myString = input("String")
for x in myString:
    if x == ' ':
        count += 1

print("No of spaces = ", count-1)
    