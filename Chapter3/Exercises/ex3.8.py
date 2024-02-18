# The variables x and y refer to numbers. Write a code segment that prompts the user for 
# an arithmetic operator and prints the value obtained by applying that operator to x and y.

x = 10
y = 2
operator = input("Enter the operator:")
if operator == '+':
    print(x + y)
elif operator== '-':
    print(x - y)
elif operator == '*':
    print(x * y)
elif operator == '/':
    print(x / y)