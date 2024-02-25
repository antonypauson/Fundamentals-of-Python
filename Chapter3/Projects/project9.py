# # Author: Antony S
# # Date: 2024-02-11
# # Program Name:Author: Antony S
# # Date: 2024-02-11
# # Program Name: SUM + AVERAGE
# Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average.
sum = 0
count = 0
while True:
    number = (input("Enter the number series or 'Enter Key' to stop:"))
    if number.strip() == "":
        break
    else:
        number = int(number)
        sum += number
        count += 1
print("Sum = ", sum)
print("Average =", sum / count)

