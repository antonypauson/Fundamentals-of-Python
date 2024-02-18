#how while loop works? 
#it executes until a false condition is reached
total = 0
data = input("Enter the number or enter key to quit:")
while data != "":
    total += int(data)
    data = input("Enter the number or enter key to quit:")

print(total)