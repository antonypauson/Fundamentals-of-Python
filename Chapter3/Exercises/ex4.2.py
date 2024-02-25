# factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while loop that computes the factorial of a given integer N

#4! = 4 * 3 * 2 * 1
digit = int(input("Enter the number:"))
count = digit
factorial = 1
while count >= 1:
    factorial = count * factorial
    count -= 1

print(factorial)