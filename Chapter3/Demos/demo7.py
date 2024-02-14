# A All grades above 89
# B All grades above 79 and below 90
# C All grades above 69 and below 80
# F All grades below 70
# Using if-elif condition

marks = int(input("Enter the marks: "))
if marks > 89: 
    print("A")
elif marks > 79 and marks < 90: 
    print("B")
elif marks > 69 and marks < 80: 
    print("C")
else: 
    print("F")
