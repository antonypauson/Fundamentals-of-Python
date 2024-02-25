# Author: Antony S
# Date: 2024-02-11
# Program Name:Author: Antony S
# Date: 2024-02-11
# Program Name: Value of Pi approximation using Leibniz

import math
n = int(input("Enter no of iterations for PI:"))
pi = 0

for i in range(n):
    deno = i * 2 + 1 #1,3,5,7,..
    numer = 1
    fraction = numer / deno
    if (i % 2 == 0):
        pi += fraction
    else:
        pi -= fraction

print(pi * 4)