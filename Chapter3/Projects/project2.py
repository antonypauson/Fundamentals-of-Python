# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Right Triangle
# Write a program that accepts the lengths of three sides of a triangle as inputs. 
# The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of 
# one side equals the sum of the squares of the other two sides.

#hypo^2 = adja^2 + oppo^2
x = int(input("1st side:"))
y = int(input("2nd side:"))
z = int(input("3rd side:"))
flag = 0
if x > y and x > z:
    if x ** 2 == y ** 2 + z ** 2:
        flag = 0
    else:
        flag = 1
elif y > z:
    if y ** 2 == x ** 2 + z ** 2:
        flag = 0
    else:
        flag = 1
else:
    if z ** 2 == x ** 2 + y ** 2:
        flag = 0
    else:
        flag = 1

if flag == 1:
    print("Not Right Angled Triangle")
else:
    print("Right Angled Triangle")
    

