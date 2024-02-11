"""
Author: Antony S
Date: 2024-02-11
The tax calculator program of the case study outputs a floating-point number 
that might show more than two digits of precision. Use the round function to 
modify the program to display at most two digits of precision in the output 
number.
"""

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDANT_DEDUCTION = 3000

gross_income = int(input("Enter gross income: "))
no_dependents = int(input("No. of dependants: "))

taxable_income = gross_income - STANDARD_DEDUCTION - DEPENDANT_DEDUCTION * no_dependents
income_tax = taxable_income * TAX_RATE

income_tax = round(income_tax, 2)

print("Your income tax = " + str(income_tax))