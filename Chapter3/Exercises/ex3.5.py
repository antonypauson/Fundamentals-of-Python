# Explain how to check for an invalid input number and prevent it being used in a 
# program. You may assume that the user enters a number

x = int(input("Enter the number between 10 and 100:"))
if x > 100:
    print("I told you to enter the number greater than 100")
elif x < 10:
    print("I told you to enter the number less than 10")
else:
    print(x)