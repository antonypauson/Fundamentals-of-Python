total = 0
data = input("Enter the number or enter key to quit:")
while True:
    if data == "":
        break
    total += int(data)
    data = input("Enter the number or enter key to quit:")

print(total)